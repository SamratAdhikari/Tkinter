# Class and Object in GUI
"""
-------------------------------
Note:
    class use gare paxi pahila root lekheko thauma aahele 'self' and tala object(window) aauxa

-------------------------------
"""

from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)

    def button(self,text):
        Button(self, text=text, command=self.click, pady=10, borderwidth=5, relief=RAISED).pack()


    # function for button
    def click(self):
        print("Button Clicked")

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.button("Click Me!!!")
    window.mainloop()