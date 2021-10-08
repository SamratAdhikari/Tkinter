# TreeView

from tkinter import *
from tkinter import ttk

# FUNCTIONS
def func1():
    item = trv.selection()
    # print(item)
    for i in item:
        print(f"Selected Item is: {trv.item(i, 'values')[0]}")

def func2():
    item = trv.selection()
    trv.delete(item)




root = Tk()

col = ("name", "surname", "id")

# Treeview
trv = ttk.Treeview(root, height=5, show="headings", columns=(0, 1, 2))
style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 13))


# addding columns
trv.column(0, width=100, anchor=CENTER)
trv.column(1, width=100, anchor=CENTER)
trv.column(2, width=50, anchor=CENTER)

# adding headings
trv.heading(0, text="Name")
trv.heading(1, text="Surname")
trv.heading(2, text="ID")

trv.pack(side=TOP, fill=BOTH)



# insert data in treeview
name = ["samrat", "naruto", "minato", "itachi"]
surname = ["adhikari", "uzumaki", "uzumaki", "uchiha"]
id = [100, 101, 102, 103]
for i in range(len(id)):
    trv.insert("", i, values=(name[i], surname[i], id[i]))

# button
btn1 = Button(root, text="GET DATA", command=func1)
btn2 = Button(root, text="DELETE DATA", command=func2)
btn1.pack(side=LEFT, padx=10, pady=10)
btn2.pack(side=RIGHT, padx=10, pady=10)




root.title("TreeView")
root.geometry("600x400")
root.mainloop()