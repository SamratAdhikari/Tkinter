# Newspaper

from tkinter import *
from PIL import Image, ImageTk

# functions
def looks(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i%100 == 0 and i!=0:
            final_text += "\n"
    return final_text
    
root = Tk()
root.title("Local Newspaper")
root.geometry("1000x1000")
root.minsize(500, 300)

texts = []
photos = []
for i in range(3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(text)

    # retrieve images
    image = Image.open(f"{i+1}.png")
    #TODO: resize these images
    image = image.resize((225, 265), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=800, height=70)
Label(f0, text="Rebel News", font="lucida 33 bold").pack()
Label(f0, text="03 July 2020", font="lucida 13 bold").pack()
f0.pack()

f1 = Frame(root, width=900, height=200, pady=14)
Label(f1, text=texts[0], padx=22, pady=22).pack(side = "left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")

f2 = Frame(root, width=900, height=200, pady=14, padx=22)
Label(f2, text=texts[1], padx=22, pady=22).pack(side = "right")
Label(f2, image=photos[1], anchor="e").pack()
f2.pack(anchor="w")

f2 = Frame(root, width=900, height=200, pady=14)
Label(f2, text=texts[2], padx=22, pady=22).pack(side = "left")
Label(f2, image=photos[2], anchor="e").pack()
f2.pack(anchor="w")


root.mainloop()