# Window Resize

from tkinter import *
import tkinter.messagebox as msg

# functions
def update():
    print("Updating the GUI")
    root.geometry(f"{width.get()}x{height.get()}")
    msg.showinfo("Done", "Window Resized")

root =Tk()
root.geometry("500x400")
root.title("Window Resize")

width = StringVar()
height = StringVar()

Entry(root, text="Width", textvariable=width).pack()
Entry(root, text="Height", textvariable=height).pack()

Button(root, text="Done", command=update).pack()

root.mainloop()