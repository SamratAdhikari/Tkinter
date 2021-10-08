# Notepad

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import *
import os
from tkinter import ttk

# Functions

def new():
    # root.mainloop()
    global file
    root.title("Untitled - Sampad")
    root.wm_iconbitmap("icon.ico")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                       filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file) + " - Sampad")
        TextArea.delete(1.0, END)
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())
def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension =".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else: # save as a new file
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))

            root.title(os.path.basename(file) + " - Sampad")
            print("File saved")

    else:
        with open(file, "w") as f:
            f.write(os.path.basename(file) + " - Sampad")



# FileMenu
def bnew(event):
    global file
    root.title("Untitled - Sampad")
    root.wm_iconbitmap("icon.ico")
    file = None
    TextArea.delete(1.0, END)

def bopenFile(event):
    global file
    file = askopenfilename(defaultextension=".txt",
                       filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file) + " - Sampad")
        TextArea.delete(1.0, END)
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())
def bsave(event):
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension =".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else: # save as a new file
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))

            root.title(os.path.basename(file) + " - Sampad")
            print("File saved")

    else:
        with open(file, "w") as f:
            f.write(os.path.basename(file) + " - Sampad")

# Edit Menu
def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

# HelpMenu
def about():
    showinfo("About us", "Sampad by Samrat")


if __name__ == '__main__':
    # Basic tkinter setup
    root = Tk()
    root.title("Untitled - Sampad")
    root.geometry("644x500")
    root.wm_iconbitmap("icon.ico")
    root.minsize(400, 300)
    root.maxsize(1366, 737)

    # Text Area
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(fill=BOTH, expand=True, padx=5, pady=1)

    # Scroll Bar
    scroll_vertical = ttk.Scrollbar(TextArea, orient='vertical')
    scroll_vertical.pack(side=RIGHT, fill=Y)
    scroll_vertical.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll_vertical.set)

    # scroll_horizontal = ttk.Scrollbar(TextArea, orient='horizontal')
    # scroll_horizontal.pack(side=BOTTOM, fill=X)
    # scroll_horizontal.config(command=TextArea.xview)
    # TextArea.config(xscrollcommand=scroll_horizontal.set)


    # Menu Bar
    menubar = Menu(root)

    # File Menu
    FileMenu = Menu(menubar, tearoff=0)

    # to open new file
    FileMenu.add_command(label="New", accelerator="Ctrl+N", command=new)

    # to open a text file
    FileMenu.add_command(label="Open", accelerator="Ctrl+O", command=openFile)

    # to save the file
    FileMenu.add_command(label="Save",accelerator="Ctrl+S", command=save)

    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=root.destroy)

    menubar.add_cascade(label="File", menu=FileMenu)
    root.config(menu=menubar)


    # Edit Menu
    EditMenu = Menu(menubar, tearoff=0)
    # Cut, Copy and Paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    menubar.add_cascade(label="Edit", menu=EditMenu)
    root.config(menu=menubar)

    # Help Menu
    HelpMenu= Menu(menubar, tearoff=0)
    HelpMenu.add_command(label="About", command=about)

    menubar.add_cascade(label="Help", menu=HelpMenu)
    root.config(menu=menubar)
    
    TextArea.bind('<Control-n>', bnew)
    TextArea.bind('<Control-o>', bopenFile)
    TextArea.bind('<Control-s>', bsave)
    
    
    root.mainloop()