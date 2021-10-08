# Grids in tkinter

        # variable classes in tkinter
        # BooleanVar, DoubleVar, IntVar, StringVar

from tkinter import *

root = Tk()
root.geometry("653x333")

user = Label(root, text = "Username")
password = Label(root, text = "Password")
user.grid(row=0)
password.grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

# button
def getvals():
    print("Thank You")
    print(f"Username: {uservalue.get()}")
    print(f"Password: {passvalue.get()}")
    with open("UserPass.txt", "a") as f:
        f.write(f"Username: {uservalue.get()}\n")
        f.write(f"Password: {passvalue.get()}\n\n")
Button(text="Submit", command=getvals).grid()


root.mainloop()