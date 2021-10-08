# Cleaner

# Modules
from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk
import os

# Functions
def confirm():
	try:
	    path = pathVar.get()
	    os.chdir(path)
	    files = os.listdir()
	    # print(files)
	    # folder = input("Enter the name of Folder: ")
	    create("Images")
	    create("Media")
	    create("Docs")
	    create("Other")

	    imgExt = [".png", ".ico", ".jpg", ".jpeg"]
	    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]
	    # print(images)

	    docExt = [".txt", ".docx", ".pdf", ".doc", ".accdb", ".pptx", ".pub", ".spv"]
	    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExt]
	    # print(docs)

	    mediaExt = [".mp3", ".mp4", ".mkv", ".ts", ".flv"]
	    media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]
	    # print(media)

	    others = []
	    for file in files:
	        ext = os.path.splitext(file)[1].lower()
	        if (ext not in mediaExt) and (ext not in imgExt) and (ext not in docExt) and os.path.isfile(file):
	            others.append(file)

	    move("Images", images)
	    move("Docs", docs)
	    move("Media", media)
	    move("Other", others)

	    askFolder = msg.askquestion("Operation Successful", "Folder Cleaned Successfully!!!\nOpen the Folder containing the Files?")
	    if askFolder == "yes":
    		folder = os.path.realpath(path)
    		os.startfile(folder)

	except Exception as e:
		msg.showinfo("Operation Unsuccessful", e)

def create(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

# gui
cleaner = Tk()
# TODO: window size
cleaner.geometry("500x300")
cleaner.title("Cleaner")
cleaner.resizable(False, False)

Label(cleaner, text="Welcome to Folder Cleaner", font="times 20 bold", bg="black", fg="white", pady=18).pack(fill=X, side=TOP)
Label(cleaner, text="Created by Samrat Adhikari\nCopyright © 2020", font="times 10", bg="black", fg="gray").pack(fill=X, side=BOTTOM)


pathVar = StringVar()
path = Label(cleaner, text="Path", font="comicsansms 15 bold")
path.place(x=50, y=120)

pathEntry = ttk.Entry(cleaner, textvar=pathVar, width=50)
pathEntry.place(x=120, y=125)





Button(cleaner, text="Confirm", bg="steel blue", fg="white", borderwidth=5, relief=RAISED, 
        font="lucida 15 bold", command=confirm).pack(side=BOTTOM, pady=20)

# main
if __name__ == "__main__":
        cleaner.mainloop()
