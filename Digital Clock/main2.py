# Digital Clock

from tkinter import *
import time

def times():
    current_day = time.strftime("%a")
    current_time = time.strftime("%H:%M:%S:%p")
    clock_lbl = Label(root, font="berlin 70", fg="white", bg="black", text=current_time)
    clock_day = Label(root, font="berlin 70", fg="white", bg="black", text=current_day)
    clock_lbl.after(200, times)
    clock_lbl.grid(row=1, column=1)
    clock_day.grid(row=0, column=1)

root = Tk()

times()


root.title("Digital Clock")
root.config(bg="black")
root.geometry("")
root.resizable(False, False)
root.mainloop()