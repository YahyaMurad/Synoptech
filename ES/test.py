import sys
import os
import shutil

# C:\Users\yahya\AppData\Local\Programs\Python\Python310\Lib\site-packages\pyke-1.1.1-py3.10.egg
output_path = "txt files\\output.txt"

def run():
    dir_path = "compiled_krb"

    with open(output_path, 'w') as file:
        file.write('')


    # Check if the directory exists
    if os.path.exists(dir_path):
        # Delete the directory
        shutil.rmtree(dir_path, ignore_errors=True)
        print(f"Deleted directory: {dir_path}")
    else:
        print(f"Directory does not exist: {dir_path}")
        
    import ES.driver as driver
    driver.bc_test()
