# Progress Bar part 2

import tkinter
from tkinter import *
from tkinter.ttk import *

# functions
# def clicked():
#     probar["value"] = 50
def clicked():
    probar2.start(10)

def stop():
    probar2.stop()

root = Tk()
root.title("Progress Bar")
root.geometry("500x300")

probar1 = Progressbar(root, length=200, orient=HORIZONTAL, maximum=100, value=10, mode="determinate")
probar1.pack()

probar2 = Progressbar(root, length=200, orient=HORIZONTAL, mode="indeterminate")
probar2.pack()



btn = tkinter.Button(root, text="Click Me", command=clicked)
btn.pack()
btn2 = tkinter.Button(root, text="Stop", command=stop)
btn2.pack()

root.mainloop()