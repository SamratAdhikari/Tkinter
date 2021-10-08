# Tkk Notebook

from tkinter import *
from tkinter import ttk


def hide():
	my_notebook.hide(1)


def show():
	my_notebook.add(frame2, text="Red Tab")


def select_red():
	my_notebook.select(1)


def select_blue():
	my_notebook.select(0)


root = Tk()

my_notebook = ttk.Notebook(root, width=500, height=500)
my_notebook.pack(fill=BOTH)

frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
frame2 = Frame(my_notebook, width=500, height=500, bg="red")

frame1.pack(fill=BOTH, expand=1)
frame2.pack(fill=BOTH, expand=1)

my_notebook.add(frame1, text="Blue Tab")
my_notebook.add(frame2, text="Red Tab")

but1 = Button(frame1, text="Hide Red Tab", command=hide)
but2 = Button(frame1, text="Show Red Tab", command=show)
but3 = Button(frame1, text="Navigate to Red Tab", command=select_red)
but4 = Button(frame2, text="Navigate to Blue Tab", command=select_blue)
but1.pack(pady=10)
but2.pack(pady=10)
but3.pack(pady=10)
but4.pack(pady=10)


root.geometry("500x500")
root.title("Notebook")
root.mainloop()