import tkinter as tk
import customtkinter
import time

def run_text_reader():


    input_path = "txt files\\input.txt"
    output_path = "txt files\\output.txt"
    technology_path = "txt files\\technology.txt"
    final_path = "txt files\\final.txt"

    customtkinter.set_default_color_theme("dark-blue")
    customtkinter.set_appearance_mode("dark")

    title_font = ("Comic Sans MS", 24)
    font = ("Tahoma", 16)


    window = customtkinter.CTk()
    window.title("Synoptech")
    window.geometry("500x500")
    window.resizable(False, False)


    output_label = customtkinter.CTkLabel(
        window,
        text="Placeholder",
        fg_color="transparent",
        wraplength=400,
        font=font
    )
    technology_label = customtkinter.CTkLabel(
        window,
        text="Placeholder",
        fg_color="transparent",
        wraplength=400,
        font=font
    )
    input_entry = customtkinter.CTkEntry(window)
    

    title_label = customtkinter.CTkLabel(
        window,
        text="Synoptech",
        fg_color="transparent",
        wraplength=400,
        font=title_font
    )

    mode_var = customtkinter.StringVar(value="dark")
    light_mode_button = customtkinter.CTkRadioButton(
        window,
        text="Light",
        variable=mode_var,
        value="light",
        font=font
    )
    dark_mode_button = customtkinter.CTkRadioButton(
        window,
        text="Dark",
        variable=mode_var,
        value="dark",
        font=font
    )
    def output():
        output_label.destroy()
        
        with open(final_path, "r") as f:
            s = f.read()
        
        label = customtkinter.CTkLabel(
            window,
            text=s,
            fg_color="transparent",
            wraplength=400,
            font=font
        )
        label.pack(padx=20, pady=20)


    def finish():
        input_entry.destroy()
        submit_button.destroy()
        technology_label.destroy()
        output_label.configure(text="Finished")
        window.after(3000, output)
        # # Get the length of the tech list

        
        # print(tech)

    def submit_input():
        user_input = input_entry.get()
        with open(input_path, 'w') as file:
            file.write(user_input)
            if output_label.cget("text").split()[0] == "Answer":
                with open(output_path, "w") as f:
                    f.write("")
        input_entry.delete(0, tk.END)  # Clear the input field
    
    submit_button = customtkinter.CTkButton(
        window,
        text="Submit",
        command=submit_input
    )

    def update_data():
        # Update the data dynamically
        output_data = get_dynamic_data()

        # Update the label texts
        output_label.configure(text=output_data)

        # Schedule the next update
        window.after(200, update_data)

    def update_tech_data():
        # Check if the label has a value
        if technology_label.cget("text"):
            with open(technology_path, "w") as g:
                g.write("")
            technology_label.configure(text="")
            window.after(5000, update_tech_data)
        else:
            # Read from technology.txt and update the label
            technology_data = get_technology_data()
            technology_label.configure(text=technology_data)
            window.after(1000, update_tech_data)

    def get_dynamic_data():
        with open(output_path, 'r') as file:
            line = file.read()
            if line == "Finished":
                finish()
            return line

    def get_technology_data():
        with open(technology_path, 'r') as file:
            return file.read()

    def show_main_window():
        # Destroy the welcome label and continue button
        title_label.destroy()
        welcome_label.destroy()
        continue_button.destroy()
        mode_label.destroy()
        light_mode_button.destroy()
        dark_mode_button.destroy()


        selected_mode = mode_var.get()
        customtkinter.set_appearance_mode(selected_mode)


        # Create a label to display the text from output.txt
        output_label.pack(padx=20, pady=20)

        # Create a label to display the text from technology.txt
        technology_label.pack(padx=20, pady=20)

        # Read the text from output.txt and technology.txt and display them in the labels
        with open(output_path, 'r') as file:
            output_text = file.read()
            output_label.configure(text=output_text)

        with open(technology_path, 'r') as file:
            technology_text = file.read()
            technology_label.configure(text=technology_text)

        # Create an entry field for user input
        input_entry.pack(padx=10, pady=10)

        # Create a button to submit the input
        submit_button.pack(padx=30, pady=30)

        # Start the data update loop
        update_data()
        update_tech_data()

    
    title_label.pack(padx=40, pady=40)
    
    welcome_label = customtkinter.CTkLabel(
        window,
        text="Welcome to Synpotech, your go-to expert system for finding optimal technologies.\n\n" + \
            "Whether you're a company or an individual, we save you time and money by providing comprehensive" + \
            "briefings and recommendations tailored to your needs. Say goodbye to endless research and" + \
            "guesswork. Our seamless navigation and user-friendly interface empower your innovation. Explore" + \
            "and propel your projects to new heights with Synpotech. Welcome aboard!",
        fg_color="transparent",
        wraplength=400,
        font=font
    )
    welcome_label.pack()

    mode_label = customtkinter.CTkLabel(
        window,
        text="Select a Mode:",
        fg_color="transparent",
        font=font)
    mode_label.pack(padx=20, pady=20)

    light_mode_button.pack()

    dark_mode_button.pack()

    # Create a continue button
    continue_button = customtkinter.CTkButton(
        window,
        text="Continue",
        command=show_main_window
    )
    continue_button.pack(padx=20, pady=20)

    # Start the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    tech = []
    run_text_reader(tech)
    
