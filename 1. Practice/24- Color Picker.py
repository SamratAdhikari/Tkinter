# Python program to create color chooser dialog box 

# importing tkinter module 
from tkinter import *

# importing the choosecolor package 
from tkinter import colorchooser 

# Function that will be invoked when the 
# button will be clicked in the main window 
def choose_color(): 

	# variable to store hexadecimal code of color 
	color_code = colorchooser.askcolor(title ="Choose color")
	label.config(text=f"Color Code:\n{color_code[0]}\n{color_code[1]}")
	root.configure(bg=f"{color_code[1]}")


root = Tk()

button = Button(root, text = "Select color", font="lucida 10 bold", bg="steelblue", fg="white", command = choose_color) 
button.pack(pady=20)

label = Label(root, font="lucida 15 bold")
label.pack(pady=10)


root.title("Color Picker")
root.geometry("500x250") 
root.mainloop() 
