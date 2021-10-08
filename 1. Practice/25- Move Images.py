# Move Images in Canvas

from tkinter import *

#Functions
def left(event):
	x = -10
	y = 0
	my_canvas.move(my_image, x, y)


def right(event):
	x = 10
	y = 0
	my_canvas.move(my_image, x, y)


def up(event):
	x = 0
	y = -10
	my_canvas.move(my_image, x, y)


def down(event):
	x = 0
	y = 10
	my_canvas.move(my_image, x, y)


root = Tk()

w = 400
h = 400
x = w
y = h

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

# Add Image to our Canvas
img = PhotoImage(file="Ball1.png").subsample(5)

my_image = my_canvas.create_image(0, 0, anchor=NW, image=img)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)


root.geometry("500x500")
root.title("Move Images")
root.mainloop()