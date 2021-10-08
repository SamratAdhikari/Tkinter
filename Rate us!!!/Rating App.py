# Rate Us!!!

from tkinter import *
import tkinter.messagebox as msg
from datetime import datetime

root = Tk()
root.geometry("500x400")
root.title("Rate Us!!!")

# func for button
def rate():
    ans = rate_scale.get()
    msg.showinfo("Rate Us!!!", f"Your rating: {ans} Stars\nThank you for rating us :)")
    with open("rate.txt", "a") as f:
        f.write(f"{getdate()} : {ans} rating\n\n")


def getdate():
    return datetime.now()

# Label
Label(root, text="Please rate our Sevice :)", font="comicsansms 13 bold").pack()

# Scale - Horizontal
rate_scale = Scale(root, from_=0, to=5, orient="horizontal", tickinterval=1)
rate_scale.pack()
Button(root, text="Submit", pady=10, padx=10, borderwidth=5, relief="raised", command=rate).pack()

root.mainloop()
