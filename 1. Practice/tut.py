from tkinter import *

root = Tk()

# GEOMETRY733x434
# "width x height"
root.geometry("733x434")

# width, height
root.minsize(500, 300)
# width, height
# root.maxsize(1366, 768)

# title
# Important Lable Options
# # text = adds the text
# # bd = backgroung
# # fg = foreground
# # font = sets the font Eg: 1. font = ("comicsansms", 15, "bold")         2. font = "comicsansms 15 bold"
# # padx = x padding
# # pady = y padding
# # relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE
root.title("My name is Samrat")


# LABLE

# title lable
title_lable = Label(text = '''Samrat is a good boy. I love Football and Basketball. I love coding too!''',
                    bg = "black", fg = "white", padx = 20, pady = 40, font = "comicsansms 15 bold",
                    borderwidth = 3, relief = RIDGE
                    )

# photo lable
# image = PhotoImage(file = "Logo.png")
# photo = Label(image = image)
# photo.pack()
# for jpg images
    # from PIL import Image, ImageTk
    # image = Image.open("photo.jpg")
    # photo = ImageTk.PhotoImage(image)

# text below title
gui_lable = Label(text="Samrat")

# Important Pack Options
# side = top, bottom, left, right
# anchor = nw
# fill = X, Y
gui_lable.pack()
title_lable.pack(side = "top", anchor = "sw", fill = X)
# fill halesi anchor narakheni hunxa

# Frame
f1 = Frame(root, bg = "purple", borderwidth = 5)
f1.pack(side = LEFT, fill = "y")
f1_label = Label(f1, text = "Project Rebel")
f1_label.pack(pady = 15)

f2 = Frame(root, borderwidth = 8, bg = "green")
f2.pack(side = BOTTOM, fill = "x")
f2_label = Label(f2, text = "Lets Rock", font = "Helvetica 20 bold", fg = "blue")
f2_label.pack(padx = 15)


# Button
 # func for button
def greet():
    print("Hello Mate")

def name():
    print("My name is Samrat Adhikari")

frame = Frame(root, borderwidth = 6, bg = "grey", relief = GROOVE)
frame.pack(side = RIGHT, anchor = "nw")

b1 = Button(frame, fg = "red", text = "Greet", command = greet)
b1.pack()
b2 = Button(frame, fg = "red", text = "Name", command = name)
b2.pack()

frame = Frame(root, borderwidth = 6, bg = "grey", relief = GROOVE)
frame.pack(side = LEFT, padx = 100)

b3 = Button(frame, fg = "red", text = "Click")
b3.pack(side = LEFT)
b4 = Button(frame, fg = "red", text = "Click")
b4.pack(side = LEFT)

# Grid
user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row = 1)
root.mainloop()
