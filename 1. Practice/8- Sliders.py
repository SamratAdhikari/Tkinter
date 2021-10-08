# Sliders in Tinter Using Scale()

from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("500x300")
root.title("Sliders")

# function for button
def get_dollar():
    print(f"We have credited {hor_slider.get()} dollars to your bank account")
    msg.showinfo("Dollars", f"We have credited {hor_slider.get()} dollars to your bank account")

Label(root, text="How many Dollars do you want?").pack()

# verticle slider
# ver_slider = Scale(root, from_=0, to=100)
# ver_slider.pack()

# horizontal slider
hor_slider= Scale(root, from_=0, to=100, orient="horizontal", tickinterval=50)
# to assign initial value in scale
hor_slider.set(50)
hor_slider.pack()
Button(root, text="Get Dollars", command=get_dollar, pady=10).pack()


root.mainloop()