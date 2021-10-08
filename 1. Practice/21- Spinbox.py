from tkinter import *
from tkinter import ttk

root = Tk()

spinVal = StringVar()
# spinVal = IntVar()
spinVal.set(0)
# my_spin = ttk.Spinbox(root, from_=0, to=1000, increment=5, textvar=spinVal)
my_spin = ttk.Spinbox(root, values=("Samrat", "Naruto", "Hinata", "Luffy"), textvar=spinVal)
my_spin.pack(pady=20)




root.title("Spinbox")
root.geometry("300x300")
root.mainloop()