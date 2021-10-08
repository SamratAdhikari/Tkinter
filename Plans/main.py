''' Plans and Projects
Author : Samrat Kumar Adhikari
Date   : 03-03-2021
Purpose: Educational Purpose
'''

# Modules
from tkinter import *
import datetime

# GUI
root = Tk()

Label(root, text="Plans and Projects")

Label(root, text="Created by Samrat Adhikari\nCopyright 2021", font="comicsansms 10 bold", bg="").pack(side=BOTTOM, fill=X, ipadx=5)

# GUI config
root.title("Plans and Projects")
root.geometry("600x500")
root.resizable(False, False)
root.mainloop()