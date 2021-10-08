# More on Tkinter

from tkinter import *

root = Tk()
root.geometry("655x444")
root.title("More on Tkinter")
root.wm_iconbitmap("icon.ico")
root.config(bg="light green")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command=root.destroy).pack() # or use 'command=quit'

root.mainloop()