# Synoptech

An expert system that helps individuals. It will provide a briefing about technologies to be used in certain tasks saving time and money spent on research to find the optimal technologies to fulfil solutions. It can be used when creating personal projects or other similar things.

## How to run Synoptech

### Installing the dependencies

Install GUI libraries
- `pip install tkinter`
- `pip install customtkinter`

Install pyke
- https://sourceforge.net/projects/pyke/files/pyke/1.1.1/, download pyke3-1.1.1 and unzip it
- Navigate to the pyke directory where the setup.py file is located
- Run the following commands `python setup.py build` `python setup.py install`
- Confirm the installation of pyke by running `pip show pyke` or by importing it in some python script `import pyke`

### Editing pyke source code

- Run the `pip show pyke` command and navigate to that directory
- Replace the `ask_tty.py` file with the file available in the repo
- On line 86 of the `ask_tty.py` file modify the paths to the txt files directory

Finally, you can run `text_reader.py` file
