# New Window

from tkinter import  *
import tkinter.messagebox as msg

# functions
def open():
    new = Toplevel()
    new.title("Secondary")
    new.geometry("600x500")
    lbl = Label(new, text="Hello World").pack()

root = Tk()
root.title("New Window")
root.geometry("644x500")

button = Button(root, text="Second Window", command=open).pack()



mainloop()