import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

technology_path = "txt files\\technology.txt"
final_path = "txt files\\final.txt"


with open(technology_path, "w") as f:
    f.write("")

with open(final_path, "w") as f:
    f.write("You should use:\n")
global tech
tech = []
def bc_test():
    engine.reset()

    engine.activate('webapp_question_rules') 
    
    try:
        with engine.prove_goal('webapp_question_rules.what_to_use($software)') as gen: 
            print(gen)
            for vars, plan in gen:
                # print(plan)
                print("You should use: %s" % (vars['software']))
                tech.append(vars['software'])
                with open(technology_path, "w") as f:
                    f.write("You should use: %s\n" % (vars['software']))

                with open(final_path, "a") as f:
                    f.write((vars['software']) + "\n")

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    

    with open(technology_path, "w") as f:
        for t in tech:
            f.write("You should use: %s" % t)

    # print()
    # print("done")
    #engine.print_stats()
