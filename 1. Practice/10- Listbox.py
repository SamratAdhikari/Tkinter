# Listbox

from tkinter import *


root = Tk()
root.geometry("500x400")
root.title("Listbox")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item")

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1

i = 0
Button(root, text="Add", command=add).pack( )

root.mainloop()
