# Canvas Widgets

from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(canvas_width, canvas_height)
root.maxsize(canvas_width, canvas_height)
root.title("Widget")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="blue")

# to create rectangle, specify coordinates of its diagonal(top left and bottom right)
can_widget.create_rectangle(100, 100, 400, 200, fill="violet")

# text
can_widget.create_text(600, 200, text="SAMRAT")

# circles/oval - coordinates similar to rectangle
can_widget.create_oval(200, 100, 300, 200, fill="navy blue")

root.mainloop()