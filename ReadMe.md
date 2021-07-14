# Simple python Gui


### Prerequisites
This code uses python ttk themes to run you can download using command:

**python -m pip install git+https://github.com/RedFantom/ttkthemes**

### How to run
Run this code using command:
(you have the option to give a file to pre-populate the gui)

**python gui.py {optional filepath}**

### Features
- In this gui you can run a file(by default it is just echoing statements back)
you may use this black screen like a terminal (for example try typing in python bye.py or cd)

- You can open a file from your directory if one was not provided at the cmd line

- The parser parses out symbolic links, varaibles, and files piped to the executable using '<' or '>'.

- You may edit these parsed out variables, add extra comments or classification, and provide an updated file name.

- Finally you may preview your changes and save the updated file to your current directory
