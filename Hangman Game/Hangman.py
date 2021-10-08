# --------------------------------GUI based Hangman Game--------------------------
# Author: Samrat Adhikari
# Date: 2020
# Purpose: Educational & Entertainment Purposes


# ----------------------------------Modules & Libraries--------------------------
from tkinter import *
from tkinter import messagebox as msg
from tkinter.tix import *
import random

# ..................................User defined module
from dictonary import translate


# ---------------------------------Backend Functions--------------------------------
def check(letter, button):

    letter = letter.upper()
    global win_count, lose_count
    exec(f"{button}.destroy()")

    # for meaning using translate function from user defined function "dictonary"

    if letter in word:
        for i in range(1, len(word)+1):
            if word[i-1] == letter:
                win_count += 1
                exec(
                    f"sil{i}.config(text='{letter.upper()}', font='lucida 35 bold')")

        if win_count == len(word):
            msg.showinfo("Congratulations!",
                         f"You Won The Game!\n\nCorrect Word: {word}")
            root.destroy()

    else:
        lose_count += 1
        exec(f'c{lose_count}.destroy()')
        exec(f"c{lose_count+1}.pack()")
        if lose_count == 6:
            msg.showinfo(
                "Sorry!", f"You Lost The Game!\n\nCorrect Word: {word}")
            root.destroy()


# ----------------------------------Game Variables---------------------------------
win_count = 0
lose_count = 0


# -----------------------------------Color Variables-------------------------------
COLOR = '#E7FFFF'


# -----------------------------------Frontend GUI---------------------------------
root = Tk()

Title = Label(root, text="Welcome to Hangman Game", font="Copperplate 25 bold")
Title.pack(side=TOP, pady=(20, 20))

# ....................................Hangman Picture Frame
hangman_frame = Frame(root)
hangman_frame.pack(pady=(0, 10))

# ...................................Hangman Images
Hangmen = ["h1", "h2", "h3", "h4", "h5", "h6", "h7"]
for hangman in Hangmen:
    exec(f"{hangman} = PhotoImage(file='images/{hangman}.png')")

# ..................................Generating Words
words_list = []  # for initial list of words

with open("words.txt") as f:
    for word in f:
        capital_word = word.strip("\n").upper()
        words_list.append(capital_word)

# .....................................Random Word
word = random.choice(words_list)

# .....................................Frame for Silhouette
word_frame = Frame(root)
word_frame.pack()


# ..................................Labeling the silhouette to the frame
for i in range(1, len(word)+1):
    exec(f"sil{i} = Label(word_frame, text='_', font='lucida 50 bold')")
    exec(f"sil{i}.pack(side=LEFT, padx=10)")

# ...................................Icon Image and Icon Message

icon = PhotoImage(file='images/i.png')
info = Label(word_frame, image=icon)
info.pack(side=LEFT, padx=10)

tip = Balloon(hangman_frame)
meaning = translate(word)
tip.bind_widget(info, balloonmsg=meaning)


# .......................................Alphabets icon
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for letter in alpha:
    exec(f"{letter} = PhotoImage(file='images/alphabets/{letter}.png')")


# ....................................Buttons for our Frame
Buttons = [['b1', 'a', 20, 430], ['b2', 'b', 90, 430],
           ['b3', 'c', 160, 430], ['b4', 'd', 230, 430],
           ['b5', 'e', 300, 430], ['b6', 'f', 370, 430], [
               'b7', 'g', 440, 430], ['b8', 'h', 510, 430],
           ['b9', 'i', 585, 430], ['b10', 'j', 650, 430], [
               'b11', 'k', 720, 430], ['b12', 'l', 790, 430],
           ['b13', 'm', 860, 430], ['b14', 'n', 20, 490], [
               'b15', 'o', 90, 490], ['b16', 'p', 160, 490],
           ['b17', 'q', 230, 490], ['b18', 'r', 300, 490], [
               'b19', 's', 370, 490], ['b20', 't', 440, 490],
           ['b21', 'u', 510, 490], ['b22', 'v', 580, 490], [
               'b23', 'w', 650, 490], ['b24', 'x', 723, 490],
           ['b25', 'y', 795, 490], ['b26', 'z', 863, 490]]


# .................................Place Alphabet Buttons
for q1 in Buttons:
    exec(f'{q1[0]}=Button(root, bd=0, command=lambda:check("{q1[1]}","{q1[0]}"),image={q1[1]})')
    exec(f'{q1[0]}.place(x={q1[2]}, y={q1[3]})')


# .................................Pack Hangman Pictures
hang = [['c1', 'h1'], ['c2', 'h2'], ['c3', 'h3'], [
    'c4', 'h4'], ['c5', 'h5'], ['c6', 'h6'], ['c7', 'h7']]
for pic in hang:
    exec(f"{pic[0]} = Label(hangman_frame, image={pic[1]})")
# ..................................initial hangman pic
c1.pack()


# ...................................Bottom Label
bottom = Label(root, text="samratmetaladhikari@gmail.com",
               bg="black", fg="white", font="lucida 10 bold")
bottom.pack(side=BOTTOM, fill=X, ipady=2)


# -------------------------------Configure Root Window-------------------------------
root.iconbitmap("images/icon.ico")
root.geometry("950x600")
root.resizable(False, False)
root.title("Hangman Game!")
root.mainloop()
