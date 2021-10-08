# Progress Bar

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msg

# Functions
val=0
def clicked():
    global val
    if val<5:
        val += 1
        proVar.set(val)
        lbl.config(text=f"Pressed {val} out of 5 times")
    else:
        msg.showwarning("Warning", "You already pressed 5 times")


root = Tk()
root.geometry("500x300")
root.title("Progress Bar")

proVar = IntVar()
proVar.set(0)
probar = Progressbar(
    root, mode="determinate", maximum=5, length=200, variable=proVar, orient=HORIZONTAL
)
probar.pack(pady=40)

btn = Button(root, text="Click me 5 times", command=clicked)

lbl = Label(root, font="consolas 16")
lbl.pack()

btn.pack(padx=20)


root.mainloop()
