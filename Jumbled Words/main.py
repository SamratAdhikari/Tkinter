# Jumbled Words
import random
from tkinter import *
import tkinter
from tkinter import messagebox as msg

answers = [
    "python",
    "java",
    "swift",
    "canada",
    "nepal",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "elnpa",
    "aiearcm",
    "odnlon",
]

num = random.randrange(0, 7, 1)

def default():
    global words, answers, num
    lbl.config(text=words[num])

def check():
    global words, answers, num
    var = e1.get()
    if var == answers[num]:
        msg.showinfo("Success", "This is the correct answer")
        reset()
    else:
        msg.showerror("Unsuccessful", "Sorry, The asnwer is incorrect")
        e1.delete(0, END)

def reset():
    global words, answers, num
    num = random.randrange(0, 7, 1)
    lbl.config(text=words[num])
    e1.delete(0, END)


root = Tk()
root.title("Jumbled Words")
root.geometry("350x400+400+150")
root.config(bg="black")

lbl = Label(root,
            text="Jumbled Words",
            font="verdana 20 bold",
            bg="black",
            fg="grey75"
            )
lbl.pack(side=TOP, pady=30)


ans = StringVar()

e1 = Entry(
    root,
    font="verdana 15",
    textvar=ans
    )
e1.pack(ipady=5, ipadx=5)

btncheck = Button(
    root,
    text="Check",
    font="comicsansms 15",
    width=10,
    bg="#4C4B4B",
    fg="#6ab04c",
    relief=GROOVE,
    borderwidth=5,
    command=check
     
)
btncheck.pack(pady=14)

btnreset = Button(
    root,
    text="Reset",
    font="comicsansms 15",
    width=10,
    bg="#4C4B4B",
    fg="#6ab04c",
    relief=GROOVE,
    command=reset
)
btnreset.pack()

default()

root.mainloop()
