# Radiobutton

from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("500x400")
root.title("Radiobuttons")

var1 = IntVar()
var1.set(1)

var2 = StringVar()
var2.set("Nothing")

def order():
    msg.showinfo("Order", f"You ordered {var1.get()}th item on the first list\nYou ordered {var2.get()}")


Label(root, text="What would you like to have?", justify="left", padx=15, font="lucida 19 bold").pack()

dict1={
    1 : "Momo",
    2 : "Pizza",
    3 : "Chowmein",
    4 : "Burger"
}

list2= ["Daal Bhat", "Roti Tarkali", "Biryani", "Dhido"]

for i in range(1, 5):
    Radiobutton(root, text=dict1[i], padx= 5, pady=5, variable=var1, value=i).pack(anchor="w")

# radio = Radiobutton(root, text="Mo:mo", padx=15, variable=var, value=1).pack(anchor="w")
# radio = Radiobutton(root, text="Daal Bhat", padx=15, variable=var, value=2).pack(anchor="w")
# radio = Radiobutton(root, text="Roti", padx=15, variable=var, value=3).pack(anchor="w")
# radio = Radiobutton(root, text="Pizza", padx=15, variable=var, value=4).pack(anchor="w")

Label(root, text="\nRadiobuttons without 'compulsory' check").pack()

for i in range(4):
    Radiobutton(root, text=list2[i], padx=5, pady=5, variable=var2, value=list2[i]).pack(anchor="sw")

Button(root, text="Order Now!!!",borderwidth=10, pady=10, command=order).pack()


root.mainloop()