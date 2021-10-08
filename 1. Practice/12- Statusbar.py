# Status Bar

from tkinter import *
import time

# functions
def upload():
    sts_var.set("Busy...")
    sbar.update()
    time.sleep(2)
    sts_var.set("Ready Now")

root = Tk()
root.geometry("500x400")
root.title("Status Bar")

sts_var = StringVar()
sts_var.set("Ready")

sbar = Label(root, textvariable=sts_var, relief=SUNKEN, anchor=W)
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload).pack()




root.mainloop()