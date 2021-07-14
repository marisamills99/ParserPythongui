from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk 
from tkinter import filedialog
import os,subprocess
import sys
from ttkthemes import ThemedStyle
entries = {}
def saveFile(entries,filenameEntry, filepath):
    #read the current file line by line 
    #check if the current line has been edited 
    #if yes write the new line  
    #if no write old line 
    
    file1 = open(filepath, 'r')
    #check if we were given a new file name
    if filenameEntry.get() != "Enter a descriptive filename here":
        if ".ksh" not in filenameEntry.get() :
            filepath=filenameEntry.get()+".ksh"
        else:
            filepath=filenameEntry.get()
        file2= open(filepath,"w+")
    else:
        file2= open("update_"+os.path.basename(filepath),"w+")
    Lines = file1.readlines()
    #check for added comment header before first line
    list1= entries[0]
    if list1[0].get() != "#add classification here":
        #check if they forgot #
        if list1[0].get()[0] != '#':
            file2.write('#')
        file2.write(list1[0].get())
        file2.write("\n")
    
    #check for extra comments added through button
    if len(list1)>1:
        i=1
        while i <len(list1):
            if list1[i].get() != "#add more comments here":
                #check if they forgot #
                if list1[i].get()[0] != '#':
                    file2.write('#')
                file2.write(list1[i].get())
                file2.write("\n")
            i+=1
    count = 1
    #iterate through the lines of the input file 
    for line in Lines:
        # if this was an edited line write the new version
        if count in entries:
            if len(entries[count]) > 1:
                list1= entries[count]
                #check if comment was added
                if list1[1].get() != "#add a comment for below line":
                    #check if they forgot #
                    if list1[1].get()[0] != '#':
                        file2.write('#')
                    file2.write(list1[1].get())
                    file2.write("\n")
                file2.write(list1[0].get())
                file2.write("\n")
            else:
                # must be a comment header line
                list1= entries[count]
                #check if they forgot #
                if list1[0].get()[0] != '#':
                    file2.write('#')
                file2.write(list1[0].get())
                file2.write("\n")
        #otherwise keep the old line     
        else:
            file2.write(line)
        count += 1
        
    file1.close()
    file2.close()
    tk.messagebox.showinfo("geomatics.",  "Saved!")
    clearFrame()
    return

def openFile():
    #open a file (by default it will ask for ksh files)

    filename= filedialog.askopenfilename(initialdir="/", title="Select Files", 
    filetypes=(("KSH files","*.ksh"), ("all files","*.*")) )
    packEntry(filename)
def addComments(newFrame):
    added = ttk.Entry(newFrame, width=50,style="Custom.TEntry")
    added.pack(pady=1,anchor=N)
    #fill the boxes with the current assignment statements
    added.insert(0,"#add more comments here")
    entries[0].append(added)

def packEntry(filename):
    clearFrame()
    
    labelfile = Label(frame, text = "Filename:",font=("Cantarell",10), bg= "dark gray")
    labelfile.pack(pady=0.5)
    filenameEntry = ttk.Entry(frame, width=50,style="Custom.TEntry")
    filenameEntry.pack()
    filenameEntry.insert(0,"Enter a descriptive filename here")

    #parse the file and get a dictionary {linenumber: assignment_statement}
    inputs= parse(filename)
    newframe = Frame(frame, bg="dark gray")
    newframe.pack()
    i,j,k,c=0,0,0,0
    for key,value in inputs.items():
        
        #not an added comment header
        if key > 0:
            string= inputs[key]
            if string[0]=="#":
                entries.setdefault(key, [])
                #found a comment header 
                commentheaderBox = ttk.Entry(frame, width=50)
                commentheaderBox.pack()
                #fill the boxes with the current assignment statements
                commentheaderBox.insert(0,string)
                entries[key].append(commentheaderBox)
                
            else:
                #add a label and a input box to gui 
                if '=' in string:
                    i=i+1
                    #label = Label(frame, text = "Variable "+ str(i) + ":",font=("Cantarell",10), bg= "dark gray")
                    #label.pack(pady=0.5)
                #check for piped inputs or outputs
                elif '<' in string or '>' in string:
                    #check if it was an input output or both in line
                    if '<' in string and '>' in string:
                        j=j+1
                        c=c+1
                        label = Label(frame, text = "Input "+ str(j) + " and Output "+str(c)+ ":",font=("Cantarell",10), bg= "dark gray")
                        label.pack(pady=0.5)
                    elif '<' in string:
                        j=j+1
                        label = Label(frame, text = "Input"+ str(j) + ":",font=("Cantarell",10), bg= "dark gray")
                        label.pack(pady=0.5)
                    elif '>' in string:
                        c=c+1
                        label = Label(frame, text = "Output "+ str(c) + ":",font=("Cantarell",10), bg= "dark gray")
                        label.pack(pady=0.5)
                # check for links
                elif 'ln -s' in string:
                    k=k+1
                    label = Label(frame, text = "Symbolic link "+ str(k) + ":",font=("Cantarell",10), bg= "dark gray")
                    label.pack(pady=0.5)
                #add a comment box
                commentBox = ttk.Entry(frame, width=50,style="Custom.TEntry")
                commentBox.pack(pady=1)

                #fill the boxes with the current assignment statements
                commentBox.insert(0,"#add a comment for below line")

                inputBox = ttk.Entry(frame, width=50)
                inputBox.pack(pady=1)

                #fill the boxes with the current assignment statements
                inputBox.insert(0,inputs[key])
            
                #add to entries dicionary the key being the line number and value being updated assignment statement and comments 
                entries.setdefault(key, [])
                entries[key].append(inputBox)
                entries[key].append(commentBox)
        else:
            entries.setdefault(key, [])
            addComment= ttk.Button(newframe, text="add extra comment line",command=lambda: addComments(newframe))
            addComment.pack()
            commentheaderBox = ttk.Entry(newframe, width=50,style="Custom.TEntry" ) 
            commentheaderBox.pack()
            #fill the boxes with the current assignment statements
            commentheaderBox.insert(0,"#add classification here")
            entries[key].append(commentheaderBox)

            
            

       

    #add a submit button to upload the changes to the file 
    submit= ttk.Button(frame, text="Save File with Changes",command=lambda: saveFile(entries,filenameEntry,filename))
    run= ttk.Button(frame, text="Run file",command=lambda: runScript(filename))
    preview= ttk.Button(frame, text="Preview file",command=lambda: previewfile(entries,filename))
    clear= ttk.Button(frame, text="Reset",command=clearFrame )
    submit.pack(pady=5)
    preview.pack(pady=5)
    run.pack(pady=5)
    clear.pack(pady=5)

def parse(filename):
    dict= {}
    dict.setdefault(0, [])
    # open and read input file
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    count = 0
    inheader=True
    label = Label(frame, text = "Header comments:",font=("Cantarell",10), bg= "dark gray")
    label.pack()
    for line in Lines:
        count += 1
        if inheader and line[0]!='#':
            #add to dictionary at 0
            dict[0]= line.strip()
            inheader=False
        elif inheader and line[0]=='#' :
            # add to dictionary at line number 
            dict[count]= line.strip()
        #add to dictionary if the line is an assignemnt and is not a comment 
        if ( '>' in line or '<' in line or 'ln -s' in line)and line[0]!='#' :
            dict[count]= line.strip()
    #The dictonary is in format {linenumber : line}
    return dict
def execute(code):
    command = configfile.get('1.0', 'end').split('\n')[-2]
    if command == 'exit':
        exit()
    configfile.insert('end', f'\n{subprocess.getoutput(command)}')
def clearFrame():
    entries.clear()
    # destroy all widgets from frame
    configfile.delete('1.0', END)
    for widget in frame.winfo_children():
       widget.destroy()
    
    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    
#simple function to echo args
def runScript(filepath):
    configfile.delete('1.0', END)
    configfile.config( bg="black", fg="white",insertbackground='white')
    
    
    # with open("output.txt", 'r') as f:
    #     configfile.insert(INSERT, f.read())
    file1 = open(filepath, 'r')
    Lines = file1.readlines()
    for line in Lines:
        if 'echo' in line:
            # echo_arg=line.split("echo",1)[1]
            # if '$' in line:
            #     arg=line.split("$",1)[1] 
            #     print(arg)
            #     echo_arg = os.environ[arg.strip()]
            #cmd = subprocess.Popen(["echo", echo_arg]
            d = dict(os.environ)
            p = subprocess.Popen(line, shell=True, env=d, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            subprocess_return = p.stdout.read()
            configfile.insert(INSERT,subprocess_return)

    configfile.bind('<Return>', execute)
def previewfile(entries,filepath):
    configfile.delete('1.0', END)
    configfile.config( bg="white", fg="black",insertbackground='black')
    file1 = open(filepath, 'r')
    file2 = open("preview.txt", 'w+')
    Lines = file1.readlines()
    #check for first comment header added before file read
    list1= entries[0]

    if list1[0].get() != "#add classification here":
        #check if they forgot #
        if list1[0].get()[0] != '#':
            file2.write('#')
        file2.write(list1[0].get())
        file2.write("\n")
    
    #check for extra added comments 
    if len(list1)>1:
        i=1
        while i <len(list1):
            if list1[i].get() != "#add more comments here":
                #check if they forgot #
                if list1[i].get()[0] != '#':
                    file2.write('#')
                file2.write(list1[i].get())
                file2.write("\n")
            i+=1
    count = 1
    #iterate through the lines of the input file 
    for line in Lines:
        # if this was an edited line write the new version
        if count in entries:
            if len(entries[count]) > 1:
                list1= entries[count]
                #check if comment was added
                if list1[1].get() != "#add a comment for below line":
                    #check if they forgot #
                    if list1[1].get()[0] != '#':
                        file2.write('#')
                    file2.write(list1[1].get())
                    file2.write("\n")
                #write the conent 
                file2.write(list1[0].get())
                file2.write("\n")
            else:
                # must be a comment header line
                list1= entries[count]
                #check if they forgot #
                if list1[0].get()[0] != '#':
                    file2.write('#')
                file2.write(list1[0].get())
                file2.write("\n")
        #otherwise keep the old line     
        else:
            file2.write(line)
        count += 1
        
    file1.close()
    file2.close()
    with open("preview.txt", 'r') as f:
        configfile.insert(INSERT, f.read())
    f.close()
    return

root = Tk()  
#give gui a title
root.title('geomatics')
root.geometry('800x600')

root.configure(bg='#fff9d1')

#background
style = ThemedStyle(root)
style.set_theme("breeze")
style.configure('Custom.TEntry', foreground='teal')


# Create A Main frame

main_frame = Frame(root)

main_frame.pack(fill=BOTH,expand=1)



# Create Frame for X Scrollbar

sec = Frame(main_frame)

sec.pack(fill=X,side=BOTTOM)



# Create A Canvas

my_canvas = Canvas(main_frame)

my_canvas.pack(side=LEFT,fill=BOTH,expand=1)



# Add A Scrollbars to Canvas

x_scrollbar = ttk.Scrollbar(sec,orient=HORIZONTAL,command=my_canvas.xview)

x_scrollbar.pack(side=BOTTOM,fill=X)

y_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
y_scrollbar.pack(side=RIGHT,fill=Y)



# Configure the canvas

my_canvas.configure(xscrollcommand=x_scrollbar.set)

my_canvas.configure(yscrollcommand=y_scrollbar.set)

my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 



# Create Another Frame INSIDE the Canvas

second_frame = Frame(my_canvas)



# Add that New Frame a Window In The Canvas

my_canvas.create_window((0,0),window= second_frame, anchor="nw")


# add a button to open a file
openFileButton= ttk.Button(second_frame, text="Open File", command=openFile )

openFileButton.pack(side=TOP, anchor=CENTER)


configfile = Text(second_frame, height=100, width=65)
configfile.pack(side = RIGHT)

#frame 
frame = Frame(second_frame,bg="dark gray" )
frame.pack(side= LEFT, anchor=NW)

if len(sys.argv) > 1:
    fn = sys.argv[1]
    if os.path.exists(fn):
        packEntry(fn)
# termf = Frame(root, height=300, width=400)

# termf.pack(fill=BOTH, expand=YES)
# wid = termf.winfo_id()
# os.system('xterm -into %d -geometry 40x20 -sb &' % wid)

#cmd = Text(root,height= 50, bg="black", fg="white",insertbackground='white')
#cmd.pack(side=BOTTOM)
#cmd.bind('<Return>', execute)
#run gui 
root.mainloop()