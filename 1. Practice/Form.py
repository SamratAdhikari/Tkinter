# Form

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
root.title("Form")

# heading and base
heading = Label(root, text="Form", font="lucida 20 bold", bg="black", fg="white", pady=15)
heading.pack(side=TOP, fill=X)
base = Label(root, text="Created by Samrat Adhikari\nCopyright @ 2020", bg="black", font="arial 7", fg="grey")
base.pack(side=BOTTOM, fill=X)

first = Label(text="First Name ", font="comicsansms 12 bold")
last = Label(text="Last Name ", font="comicsansms 12 bold")
age = Label(text="Age", font="comicsansms 12 bold")
gender = Label(text="Gender", font="comicsansms 12 bold")
first.place(x=50, y=80)
last.place(x=50, y=110)
age.place(x=50, y=140)
gender.place(x=200, y=140)

# first and last name and age and gender values
firstVar = StringVar()
lastVar = StringVar()
ageVar = IntVar()
genderVar = StringVar()
ageVar.set(10)
genderVar.set("None")

# first and last name and age and gender entries
firstEntry = ttk.Entry(root, textvar=firstVar)
lastEntry = ttk.Entry(root, textvar=lastVar)
ageEntry = ttk.Entry(root, textvar=ageVar, width="5")
firstEntry.place(x=180, y=80)
lastEntry.place(x=180, y=110)
ageEntry.place(x=100, y=140)

# Radiobutton for gender
gender_list = ["Male", "Female"]
male = Radiobutton(text=gender_list[0], font="lucida 13", variable=genderVar,
                   value=gender_list[0]).place(x=270, y=139)
female = Radiobutton(text=gender_list[1], font="lucida 13", variable=genderVar,
                   value=gender_list[1]).place(x=340, y=139)
# seperator
# Label(root, text="", pady=2, bg="black").pack(fill=)

# button
Button(text="Register", width="10", relief=RAISED, bg="steel blue",
       fg="white", font="comicsansms 9 bold", borderwidth=5, height="2").place(x=200, y=400)


root.mainloop()