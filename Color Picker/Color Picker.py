# Python program to create color chooser dialog box 

# importing tkinter module 
from tkinter import *
import pyperclip

# importing the choosecolor package 
from tkinter import colorchooser 

# Function that will be invoked when the 
# button will be clicked in the main window 
def choose_color():
	global code

	# variable to store hexadecimal code of color 
	color_code = colorchooser.askcolor(title ="Choose color")
	label.config(text=f"Color Code:\n{color_code[1]}")
	root.config(bg=f"{color_code[1]}")

	code = color_code[1]
	btn.config(text="Copy", bg="spring green")
	btn.pack(side=BOTTOM, pady=(0, 10))


def copyColor():
	pyperclip.copy(code)
	btn.config(text="Copied", bg="salmon")

root = Tk()

button = Button(root, text = "Select color", font="lucida 10 bold", bg="#a8aaff", relief=RAISED, borderwidth=3, fg="black", command=choose_color) 
button.pack(pady=10)
btn = Button(root, text="Copy", font="lucida 10 bold", width=10, bg="spring green", relief=RAISED, borderwidth=3, fg="black", command=copyColor)

label = Label(root, font="lucida 15 bold", bg="white")
label.pack(pady=(20, 10))


root.title("Color Picker")
root.wm_iconbitmap("icon.ico")
root.resizable(False, False)
root.geometry("400x200") 
root.mainloop() 
