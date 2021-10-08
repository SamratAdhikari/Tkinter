# Handling Events

from tkinter import *

root = Tk()
root.title("Events")
root.geometry("600x350")


widget = Button(root, text="Click me Please...")
widget.pack()

# event handling
def samrat(event):
    print(f"You clicked the button at {event.x}, {event.y}")
widget.bind("<Button-1>", samrat)
widget.bind("<Double-1>", quit)


root.mainloop()