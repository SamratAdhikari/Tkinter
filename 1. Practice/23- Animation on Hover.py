# Animation on Mouse Hover

from tkinter import *


#Functions
def change(e):
	my_pic = PhotoImage(file="Ball2.png").subsample(2)
	lbl.config(image=my_pic)
	lbl.image = my_pic


def back(e):
	my_pic = PhotoImage(file="Ball1.png").subsample(3)
	lbl.config(image=my_pic)
	lbl.image = my_pic


root = Tk()

my_pic = PhotoImage(file="Ball1.png").subsample(3)
lbl = Label(root, image=my_pic)
lbl.pack(pady=20)

lbl.bind("<Enter>", change)
lbl.bind("<Leave>", back)


root.geometry("500x500")
root.title("Animation on Hover")
root.mainloop()
