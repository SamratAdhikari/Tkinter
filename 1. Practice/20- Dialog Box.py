from tkinter import *
from tkinter import filedialog
import os


a = os.getcwd()


def select_file():
    filedialog.askopenfilename(
        initialdir=a,
        title="Select a file",
        filetypes=(("png files", "*.png"), ("all files", "*.*"))
    )


def select_folder():
    folder = filedialog.askdirectory(initialdir=a,
                                     title="Select the path")
    Label(text=folder).pack(side=BOTTOM)


root = Tk()
root.geometry("400x400")


file_btn = Button(text="Select Files", command=select_file)
folder_btn = Button(text="Select Folder", command=select_folder)

file_btn.pack()
folder_btn.pack()

# root.filename = filedialog.askopenfilename( initialdir="D:\SAMRAT
# FILE\Documents\Programing\Programming\Python\Practice and Programs\Tkinter Module\1. Practice", title="Select a
# file", filetypes=(("png files", "*.png"), ("all files", "*.*")) )
#
# root.directory = filedialog.askdirectory( initialdir = "D:\SAMRAT
# FILE\Documents\Programing\Programming\Python\Practice and Programs\Tkinter Module\1. Practice" )

# print(root.directory)

root.title("Dialog box")
root.mainloop()
