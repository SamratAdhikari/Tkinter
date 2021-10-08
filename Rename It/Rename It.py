# Rename It

# Modules
from tkinter import *
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
import os
from datetime import datetime
from natsort import natsorted
from tkinter import filedialog

# initial location
location = os.getcwd()


# Functions
def magic():
    global extension
    extension.clear()
    final = []
    file_path = pathVal.get()
    file_format = f".{formatVal.get()}"
    file_front = frontVal.get()
    initial_no = initialVal.get()
    f = open(f"{location}\\RenameLog.txt", "a")

    try:
        # Setting the extensions
        split_format = file_format.split(",")
        for i in split_format:
            if i[0] == ".":
                i = i.split(".")[1]
            i = i.strip()
            extension.add(f".{i}")

        # Working with os module to rename the file(s)
        os.chdir(file_path)
        files = natsorted(os.listdir(file_path))
        f.write(f"\n\n{datetime.now().date()} | {datetime.now().strftime('%H:%M:%S')} :\n")
        for file in files:
            if os.path.splitext(file)[1] in extension:
                final.append(file)

        for index, file in enumerate(final, start=initial_no):
            if len(final) >= 10 and len(files) < 100:
                if index < 10:
                    f.write(f"\t{file}  -->  {file_front} - 0{index}{os.path.splitext(file)[1]}\n")
                    os.rename(file, f"{file_front} - 0{index}{os.path.splitext(file)[1]}")
                else:
                    f.write(f"\t{file}  -->  {file_front} - {index}{os.path.splitext(file)[1]}\n")
                    os.rename(file, f"{file_front} - {index}{os.path.splitext(file)[1]}")

            elif len(final) >= 100:
                if index < 10:
                    f.write(f"\t{file}  -->  {file_front} - 00{index}{os.path.splitext(file)[1]}\n")
                    os.rename(file, f"{file_front} - 00{index}{os.path.splitext(file)[1]}")
                elif 100 > index >= 10:
                    f.write(f"\t{file}  -->  {file_front} - 0{index}{os.path.splitext(file)[1]}\n")
                    os.rename(file, f"{file_front} - 0{index}{os.path.splitext(file)[1]}")
                else:
                    f.write(f"\t{file}  -->  {file_front} - {index}{os.path.splitext(file)[1]}\n")
                    os.rename(file, f"{file_front} - {index}{os.path.splitext(file)[1]}")

            elif len(final) < 10:
                f.write(f"\t{file}  -->  {file_front} - {index}{os.path.splitext(file)[1]}\n")
                os.rename(file, f"{file_front} - {index}{os.path.splitext(file)[1]}")

        f.close()

        # to open the folder
        askFolder = msg.askquestion("Operation Successful",
                                    "File(s) Renamed Successfully!!!\nOpen the Folder containing the Files?")
        if askFolder == "yes":
            folder = os.path.realpath(file_path)
            os.startfile(folder)

    except Exception as e:
        msg.showerror("Operation Failed", e)


def showlog():
    os.chdir(location)
    os.startfile(f"{location}\\RenameLog.txt")


# showlog()
def about():
    msg.showinfo("About Us", "Program by Samrat Adhikari\n\nFor Help and Inquiries, visit:\n"
                             "samratmetaladhikari@gmail.com")


def readme():
    os.chdir(location)
    os.startfile(f"{location}\\Readme.txt")


def updateit():
    msg.showinfo("Check for Update", "You are using the latest version\n\nVersion 2.0.1")


def quitpro():
    root.destroy()


def select_folder():
    folder = filedialog.askdirectory(parent=root, title="Select the Folder")
    pathVal.set(folder)


def choose_format():
    global extension, win

    for i in extVal:
        i.set(0)

    extension.clear()
    win = Toplevel()

    video_frame = ttk.LabelFrame(win, text="Video")
    audio_frame = ttk.LabelFrame(win, text="Audio")
    image_frame = ttk.LabelFrame(win, text="Image")
    document_frame = ttk.LabelFrame(win, text="Document")
    video_frame.grid(row=0, column=0, padx=(8, 0), pady=10)
    audio_frame.grid(row=1, column=0, padx=(8, 0), pady=(0, 10), ipadx=5)
    image_frame.grid(row=1, column=1, padx=(8, 0), pady=(0, 10))
    document_frame.grid(row=0, column=1, padx=(8, 0), pady=10, ipadx=3)

    class Extensions:
        def __init__(self, frame, onvalue, Val, row, column):
            self.frame = frame
            self.onvalue = onvalue
            self.Val = Val
            text = onvalue.replace(".", "")
            self.row = row
            self.column = column
            self.check = ttk.Checkbutton(frame, text=text, variable=Val, onvalue=onvalue, offvalue="")
            self.check.grid(row=row, column=column, sticky=W, pady=5, padx=5)

    # Videos
    Extensions(video_frame, ".avi",  aviVal,  0, 0)
    Extensions(video_frame, ".flv",  flvVal,  0, 1)
    Extensions(video_frame, ".mkv",  mkvVal,  0, 2)
    Extensions(video_frame, ".mov",  movVal,  1, 0)
    Extensions(video_frame, ".mp4",  mp4Val,  1, 1)
    Extensions(video_frame, ".mts",  mtsVal,  1, 2)
    Extensions(video_frame, ".ts",   tsVal,   2, 0)
    Extensions(video_frame, ".webm", webmVal, 2, 1)
    Extensions(video_frame, ".wmv",  wmvVal,  2, 2)

    # Audios
    Extensions(audio_frame, ".aac",  aacVal,  0, 0)
    Extensions(audio_frame, ".aiff", aiffVal, 0, 1)
    Extensions(audio_frame, ".au",   auVal,   0, 2)
    Extensions(audio_frame, ".flac", flacVal, 1, 0)
    Extensions(audio_frame, ".m4a",  m4aVal,  1, 1)
    Extensions(audio_frame, ".mp3",  mp3Val,  1, 2)
    Extensions(audio_frame, ".ogg",  oggVal,  2, 0)
    Extensions(audio_frame, ".wav",  wavVal,  2, 1)
    Extensions(audio_frame, ".wma",  wmaVal,  2, 2)

    # Images
    Extensions(image_frame, ".bmp",  bmpVal,  0, 0)
    Extensions(image_frame, ".gif",  gifVal,  0, 1)
    Extensions(image_frame, ".heic", heicVal, 0, 2)
    Extensions(image_frame, ".ico",  icoVal,  1, 0)
    Extensions(image_frame, ".jpg",  jpgVal,  1, 1)
    Extensions(image_frame, ".png",  pngVal,  1, 2)
    Extensions(image_frame, ".psd",  psdVal,  2, 0)
    Extensions(image_frame, ".raw",  rawVal,  2, 1)
    Extensions(image_frame, ".tiff", tiffVal, 2, 2)

    # Documents
    Extensions(document_frame, ".cbr" , cbrVal , 0, 0)
    Extensions(document_frame, ".docx", docxVal, 0, 1)
    Extensions(document_frame, ".db"  , dbVal  , 0, 2)
    Extensions(document_frame, ".txt" , txtVal , 1, 0)
    Extensions(document_frame, ".odt" , odtVal , 1, 1)
    Extensions(document_frame, ".pdf" , pdfVal , 1, 2)
    Extensions(document_frame, ".rar" , rarVal , 2, 0)
    Extensions(document_frame, ".rtf" , rtfVal , 2, 1)
    Extensions(document_frame, ".zip" , zipVal , 2, 2)

    ttk.Button(win, text="Select", command=ext).place(x=160, y=260)

    win.geometry("382x300")
    win.resizable(False, False)
    win.focus()
    win.mainloop()


def ext():
    win.destroy()
    global extension
    
    for item in extVal:
        extension.add(item.get())
        
    try:
        extension.remove("0")
        extension.remove("")
        print(extension)
    except Exception as e:
        pass

    ext_show = str(extension).replace("{", "").replace("'", "").replace("}", "").replace(".", "")
    print(ext_show)
    if ext_show != "set()":
    # if ext_show != "0":
        formatVal.set(ext_show)


width, height = 590, 470

root = Tk()

# Menu
menubar = Menu(root)

m1 = Menu(menubar, tearoff=0)
m1.add_command(label="Show Log", command=showlog)
m1.add_command(label="Update", command=updateit)
m1.add_separator()
m1.add_command(label="Exit", command=quitpro)
menubar.add_cascade(label="Files", menu=m1)
root.config(menu=menubar)

m2 = Menu(root, tearoff=0)
m2.add_command(label="Readme", command=readme)
m2.add_separator()
m2.add_command(label="About Us", command=about)
menubar.add_cascade(label="Help", menu=m2)
root.config(menu=menubar)

# label title
Label(root, text="Welcome to Rename It !", pady=3, bg="black", fg="grey90", font="comicsansms 15 bold").pack(fill=X)
Label(root, text="Please proceed as guided below...", bg="black", fg="grey90", font="comicsansms 12 bold").pack(fill=X)

# Label base
Label(root, text="Created by Samrat Adhikari\nCopyright © 2020",
      font="arial 8", bg="black", fg="grey", anchor=CENTER).pack(side=BOTTOM, fill=X)

# Entry
# topics
path = Label(root, text="Path of Files", font="lucida 13 bold")
formate = Label(root, text="File Format", font="lucida 13 bold")
front = Label(root, text="Front Text", font="lucida 13 bold")
initial = Label(root, text="Initial number", font="lucida 13 bold")

path.place(x=50, y=110)
formate.place(x=50, y=143)
front.place(x=50, y=176)
initial.place(x=50, y=209)

# inputs
pathVal = StringVar()
formatVal = StringVar()
frontVal = StringVar()
initialVal = IntVar()
initialVal.set(1)

pathEntry = ttk.Entry(root, textvar=pathVal, width=30, font="comicsansms 13")
formatEntry = ttk.Entry(root, textvar=formatVal, width=30, font="comicsansms 13")
frontEntry = ttk.Entry(root, textvar=frontVal, width=30, font="comicsansms 13")
initialEntry = ttk.Spinbox(root, textvar=initialVal, from_=-1000, to=1000, width=29, font="comicsansms 13")

pathEntry.place(x=180, y=110)
formatEntry.place(x=180, y=143)
frontEntry.place(x=180, y=176)
initialEntry.place(x=180, y=209)
pathEntry.focus()

# Select Folder Button
selectFolder = ttk.Button(root, text="Select Folder", command=select_folder)
selectFolder.place(x=455, y=110)
# Format Choose Button
chooseFormat = ttk.Button(root, text="Choose Ext", command=choose_format)
chooseFormat.place(x=455, y=143)

# Confirmation Button
Button(root, text="Confirm", bg="steel blue", fg="white", font="comicsansms 15 bold", command=magic,
       borderwidth=5, ).place(x=250, y=270)

# Warning
sbar = Label(root, font="lucida 10 bold", relief=RIDGE, anchor=CENTER, pady=10, bg="coral2", fg="black",
             text="Warning!!!\n"
                  "Once Renamed, it cant be undone\n"
                  "Do not to type '.' before exts & use ',' to separate the exts!")
sbar.pack(side=BOTTOM, padx=20, pady=20, fill=X)

# Extensions Values
# Video Extensions
mp4Val = StringVar()
aviVal = StringVar()
webmVal = StringVar()
tsVal = StringVar()
mkvVal = StringVar()
movVal = StringVar()
flvVal = StringVar()
wmvVal = StringVar()
mtsVal = StringVar()

# Audio Val
mp3Val = StringVar()
auVal = StringVar()
wavVal = StringVar()
aiffVal = StringVar()
aacVal = StringVar()
oggVal = StringVar()
wmaVal = StringVar()
flacVal = StringVar()
m4aVal = StringVar()

# Image Val
jpgVal = StringVar()
pngVal = StringVar()
icoVal = StringVar()
gifVal = StringVar()
heicVal = StringVar()
bmpVal = StringVar()
rawVal = StringVar()
tiffVal = StringVar()
psdVal = StringVar()

# Document Val
txtVal = StringVar()
docxVal = StringVar()
rarVal = StringVar()
cbrVal = StringVar()
zipVal = StringVar()
rtfVal = StringVar()
odtVal = StringVar()
pdfVal = StringVar()
dbVal = StringVar()

extension = set()

# Universal Variables
extVal = [mp4Val, aviVal, webmVal, tsVal, mkvVal, movVal, flvVal, wmvVal, mtsVal,
          mp3Val, auVal, wavVal, aiffVal, aacVal, oggVal, wmaVal, flacVal, m4aVal,
          jpgVal, pngVal, icoVal, gifVal, heicVal, bmpVal, rawVal, tiffVal, psdVal,
          txtVal, docxVal, rarVal, cbrVal, zipVal, rtfVal, odtVal, pdfVal, dbVal]

if __name__ == "__main__":
    root.geometry(f"{width}x{height}")
    root.resizable(False, False)
    root.title("Rename It")
    root.wm_iconbitmap("icon.ico")
    root.mainloop()
