# Menu and Submenu
from tkinter import *

root = Tk()
root.geometry("700x500")
root.title("Menu")

# command funcs
def file():
    print("You are in Files")


## For non-dropdown menu---
    # mymenu = Menu(root)
    # mymenu.add_command(label="File", command=file)
    # mymenu.add_command(label="Exit", command=quit)


# For dropdown menu---
menubar = Menu(root)

# Files Menu
m1 = Menu(menubar, tearoff=0)
m1.add_command(label="New Project", command=file)
m1.add_command(label="Save", command=file)
m1.add_command(label="Save As", command=file)
m1.add_command(label="Print", command=file)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
root.config(menu=menubar)
# to pack the menu
menubar.add_cascade(label="Files", menu=m1)
# Edit menu
m3 = Menu(menubar, tearoff=0)
m3.add_command(label="Copy", command=file)
m3.add_command(label="Cut", command=file)
m3.add_command(label="Paste", command=file)
m3.add_command(label="Find", command=file)
root.config(menu=menubar)
menubar.add_cascade(label="Edit", menu=m3)

# Options menu
m2 = Menu(menubar, tearoff=0)
m2.add_command(label="Settings", command=file)
m2.add_command(label="Theme", command=file)
m2.add_command(label="Shortcuts", command=file)
m2.add_command(label="Help", command=file)
root.config(menu=menubar)
menubar.add_cascade(label="Options", menu=m2)

root.mainloop()