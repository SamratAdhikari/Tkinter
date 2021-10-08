# title
# Tic Tac Toe

# modules
from tkinter import *
from tkinter import messagebox as msg


# Functions
def winner():
    # For X
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="spring green")
        b2.config(bg="spring green")
        b3.config(bg="spring green")
        msg.showinfo("Winner", "Player 'X' is the winner !!!")

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="spring green")
        b4.config(bg="spring green")
        b7.config(bg="spring green")
        msg.showinfo("Winner", "Player 'X' is the winner !!!")

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="spring green")
        b5.config(bg="spring green")
        b9.config(bg="spring green")
        msg.showinfo("Winner", "Player 'X' is the winner !!!")

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="spring green")
        b5.config(bg="spring green")
        b8.config(bg="spring green")
        msg.showinfo("Winner", "Player 'X' is the winner !!!")

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="spring green")
        b6.config(bg="spring green")
        b9.config(bg="spring green")
        msg.showinfo("Winner", "Player 'X' is the winner !!!")

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="spring green")
        b5.config(bg="spring green")
        b7.config(bg="spring green")
        msg.showinfo("Winner", "Player 'X' is the winner !!!")

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="spring green")
        b5.config(bg="spring green")
        b6.config(bg="spring green")
        msg.showinfo("Winner", "Player 'X' is the winner !!!")

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="spring green")
        b8.config(bg="spring green")
        b9.config(bg="spring green")
        msg.showinfo("Winner", "Player 'X ' is the winner !!!")

    # For O
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="spring green")
        b2.config(bg="spring green")
        b3.config(bg="spring green")
        msg.showinfo("Winner", "Player 'O' is the winner !!!")

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="spring green")
        b4.config(bg="spring green")
        b7.config(bg="spring green")
        msg.showinfo("Winner", "Player 'O' is the winner !!!")

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="spring green")
        b5.config(bg="spring green")
        b9.config(bg="spring green")
        msg.showinfo("Winner", "Player 'O' is the winner !!!")

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="spring green")
        b5.config(bg="spring green")
        b8.config(bg="spring green")
        msg.showinfo("Winner", "Player 'O' is the winner !!!")

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="spring green")
        b6.config(bg="spring green")
        b9.config(bg="spring green")
        msg.showinfo("Winner", "Player 'O' is the winner !!!")

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="spring green")
        b5.config(bg="spring green")
        b7.config(bg="spring green")
        msg.showinfo("Winner", "Player 'O' is the winner !!!")

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="spring green")
        b5.config(bg="spring green")
        b6.config(bg="spring green")
        msg.showinfo("Winner", "Player 'O' is the winner !!!")

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="spring green")
        b8.config(bg="spring green")
        b9.config(bg="spring green")
        msg.showinfo("Winner", "Player 'O' is the winner !!!")

    # For draw
    elif b1["text"] != "" and b2[
        "text"] != "" and b3["text"] != "" and b4 != "" and b4["text"] != "" and b5["text"] != "" and b6[
        "text"] != "" and b7["text"] != "" and b8["text"] != "" and b9["text"] != "":
        msg.showinfo("Draw", "Its a Draw !!!")



# to check the Xs and Os
def checker(btn):
    global i
    if btn["text"] == "":
        if i == "X":
            i = "O"
            btn["text"] = "X"
            winner()
        elif i == "O":
            i = "X"
            btn["text"] = "O"
            winner()

#to rest the buttons and their colours
def reset():
    b1["text"] = ""
    b2["text"] = ""
    b3["text"] = ""
    b4["text"] = ""
    b5["text"] = ""
    b6["text"] = ""
    b7["text"] = ""
    b8["text"] = ""
    b9["text"] = ""

    b1.config(bg=b)
    b2.config(bg=b)
    b3.config(bg=b)
    b4.config(bg=b)
    b5.config(bg=b)
    b6.config(bg=b)
    b7.config(bg=b)
    b8.config(bg=b)
    b9.config(bg=b)


# Colours
b = "sky blue"

root = Tk()

# frame for our buttons
frm = Frame(root, height=450, width=600, padx=5, pady=5, bg="midnight blue")
frm.place(x=0, y=0)

# Test codes
# i = 'X'
# for x in range(9):
#     b = Button(frm, text="", font="times 26 bold", height=3, width=8, bg=b, command=lambda: checker(b1))
#     for x in range(3):
        



                                        # 

# Buttons
i = "X"
b1 = Button(frm, text="", font="times 26 bold", height=3, width=8, bg=b, command=lambda: checker(b1))
b2 = Button(frm, text="", font="times 26 bold", height=3, width=8, bg=b, command=lambda: checker(b2))
b3 = Button(frm, text="", font="times 26 bold", height=3, width=8, bg=b, command=lambda: checker(b3))
b4 = Button(frm, text="", font="times 26 bold", height=3, width=8, bg=b, command=lambda: checker(b4))
b5 = Button(frm, text="", font="times 26 bold", height=3, width=8, bg=b, command=lambda: checker(b5))
b6 = Button(frm, text="", font="times 26 bold", height=3, width=8, bg=b, command=lambda: checker(b6))
b7 = Button(frm, text="", font="times 26 bold", height=3, width=8, bg=b, command=lambda: checker(b7))
b8 = Button(frm, text="", font="times 26 bold", height=3, width=8, bg=b, command=lambda: checker(b8))
b9 = Button(frm, text="", font="times 26 bold", height=3, width=8, bg=b, command=lambda: checker(b9))
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

# Reset Button
b0 = Button(root, text="RESET", font="arial 15 bold", height=2, width=20, bg="indian red", fg="black", command=reset)
b0.place(x=150, y=480)


# GUI size, icon and title and colour
root.title("Tic Tac Toe")
root.iconbitmap("icon.ico")
root.geometry("543x575+250+20")
root.config(bg="midnight blue")
root.resizable(False, False)
root.mainloop()
