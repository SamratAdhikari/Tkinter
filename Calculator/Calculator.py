# Calculator

from tkinter import *


# Functions
def click(event):
    global scvalue
    text = event.widget.cget("text")
    # print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                # print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "AC":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("600x550")
root.minsize(600, 550)
root.maxsize(600, 550)
root.title("Calculator")
root.wm_iconbitmap("icon.ico")

Label(root, text="Calculator by Samrat", borderwidth=2, padx=20, pady=10, font="comicsansms 10 bold").pack()


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=10, pady=10, padx=30)

f1 = Frame(root, bg="grey")
f1.pack()
for i in range(1,6):
    b=Button(f1, text=str(i), padx=10, pady=5, font="lucida 30 bold", bg="light green")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)

f2 = Frame(root, bg="grey")
f2.pack()
for i in range(6, 11):
    if i == 10:
        i = 0
    b = Button(f2, text=str(i), padx=10, pady=5, font="lucida 30 bold", bg="light green")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)

f3 = Frame(root, bg="grey")
f3.pack()
b = Button(f3, text="+", padx=9, pady=5, font="lucida  30 bold", bg="light blue")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f3, text="-", padx=15, pady=5, font="lucida  30 bold", bg="light blue")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f3, text="*", padx=13, pady=5, font="lucida  30 bold", bg="light blue")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f3, text="/", padx=16, pady=5, font="lucida  30 bold", bg="light blue")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f3, text="=", padx=9, pady=5, font="lucida  30 bold", bg="light goldenrod")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f4 = Frame(root, bg="grey")
f4.pack()
b = Button(f4, text="AC", padx=10, pady=5, font="lucida  20 bold", bg="salmon")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

root.mainloop()