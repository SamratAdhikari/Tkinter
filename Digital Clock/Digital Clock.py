# Digital Clock

# Modules
import sys
from tkinter import *
import time

# Functions
def times():
    current = time.strftime("%H:%M:%S")
    clock.config(text=current)
    clock.after(200, times)


root = Tk()
root.config(bg="grey7")
root.geometry("450x250")
clock = Label(root, font="times 50 bold", bg="black", fg="mint cream")
clock.grid(row=2, column=2, pady=25, padx=100)
times()

digital = Label(root, text="Digital Clock", font="times 24 bold", bg="black", fg="steel blue")
digital.grid(row=0, column=2)

notation = Label(root, text="  Hours      Minutes    Seconds", font="times 15 bold", bg="black", fg="cyan4")
notation.grid(row=3, column=2)

root.resizable(False, False)
root.iconbitmap("icon.ico")
root.title("Digital Clock")
root.mainloop()