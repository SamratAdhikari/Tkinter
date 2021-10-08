# Dropdown Menus

from tkinter import *
from tkinter import ttk

def show():
    Label(root, text=clicked.get()).pack()

def comboclick(event):
       Label(root, text=combo.get()).pack()

root = Tk()

clicked = StringVar()
opt = ["Sunday",
       "Monday",
       "Tuesday",
       "Wednesday",
       "Thursday",
       "Friday",
       "Saturday"
       ]

drop = ttk.OptionMenu(root, clicked, "Day", *opt)
drop.pack()

btn = Button(root, text="Day", command=show)
btn.pack(pady=10, ipadx=20, ipady=20)


combo = ttk.Combobox(root, value=opt)
combo.current(0)
combo.bind("<<ComboboxSelected>>", comboclick)
combo.pack()

root.title("Dropdown Menus")
root.geometry("500x500")
root.mainloop()