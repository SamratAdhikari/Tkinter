# Scrollbar

from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Scrollbar")

Label(root, text="List of items", font="comicsansms 13 bold", pady=10, borderwidth=10).pack(side=TOP)


# to connect scrollbar to a widget:
## 1. widget(yscrollcommand = scrollbar.set)
## 2. scrollbar.config(command=widget.yview)

scb = Scrollbar(root)
scb.pack(side=RIGHT, fill=Y)

# scroll for listbox
lbx = Listbox(root, yscrollcommand=scb.set) ## 1. widget(yscrollcommand = scrollbar.set)
for i in range(1, 201):
    lbx.insert(END, f"Item {i}")
lbx.pack(fill=BOTH, padx=10)
scb.config(command=lbx.yview) ## 2. scrollbar.config(command=widget.yview)

# scroll for text
text = Text(root)
text.pack(fill=BOTH, padx=10, pady=10)


root.mainloop()