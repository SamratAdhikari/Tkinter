# Message Box

from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("500x400")

# Functions
def com():
    print("Hello world")

def help():
    print("You are inside Help")
    msg.showinfo("Help", "Please Email us at\nsamratinternational@gmail.com")

def checkUpdate():
    print("You are inside Check Update")
    msg.showinfo("Check Update", "You have the latest version of the software\nVersion 3.0.1")

def rate():
    print("You are inside Rate Us")
    value = msg.askquestion("Rate Us", "Was our Program helpful?")
    print(value)
    if value == "yes":
        ans = "Great! Please Rate us on AppStore"
    elif value=="no":
        ans = "Tell us what went wrong..."
    msg.showinfo("Experience", ans)

def flirt():
    ask = msg.askretrycancel("Befriend her!", "Sorry! aint gonna happen...")
    if ask:
        msg.showinfo("Retry", "Nothing changes even if you Retry!")
    else:
        msg.showinfo("Cancel", "You were wise enough to not mess with her\n"
                               "Cause she has a boyfriend that plays Rugby")
# menus
mainmenu= Menu(root)

# Files
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New File", command=com)
m1.add_command(label="Save", command=com)
m1.add_command(label="Save As", command=com)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

# Edit
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Copy", command=com)
m2.add_command(label="Cut", command=com)
m2.add_command(label="Paste", command=com)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

# MessageBox Menu
m3 = Menu(root, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Check Update", command=checkUpdate)
m3.add_command(label="Rate Us", command=rate)
m3.add_separator()
m3.add_command(label="Flirt", command=flirt)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="MsgBox", menu=m3)

root.mainloop()