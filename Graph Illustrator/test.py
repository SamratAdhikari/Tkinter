'''Graph Illustrator
Autor  : Samrat Adhikari
Date   : 16/02/2021
Purpose: Educational Purpose'''

# Modules
import os
from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
import backend # custom made module


# Variables and Main Lists
itemList = []

# Functions
y = 38
x = 1
def addCommand(): # adds new entry widgets for equation and its range
	global y, x, itemList

	# Class
	eqn  = eqnVar.get()
	low  = lowVar.get()
	high = highVar.get()

	class Equations:

		def __init__(self, eqn, low, high, y):
			self.eqnEntry   = eqn					
			self.lowEntry   = low									
			self.highEntry  = high
			self.yaxis      = y

			eqnEntry  = ttk.Entry(inputFrame, width=20, textvar=eqn,  font="comicsansms 13")
			lowEntry  = ttk.Entry(inputFrame, width=5 , textvar=low,  font="comicsansms 13")
			highEntry = ttk.Entry(inputFrame, width=5 , textvar=high, font="comicsansms 13")
			dashLabel = Label(inputFrame, text="-", font="comicsansms 13 bold")

			eqnEntry.place(x=20, y=y)
			lowEntry.place(x=240, y=y)
			# self.dashLabel.place(x=295, y=y)
			highEntry.place(x=313, y=y)

	itemList.append(x)

	# entry = Equations(eqn, low, high, y)
	entry = Equations(x, 0, 5, y)

	y += 30
	x += 1

	print(itemList, y)


def generateCommand(): # generates graphs through matplotlib
	# get all the values from the Entry Widgets
	eqn    = eqnVar.get()
	low    = lowVar.get()
	high   = highVar.get()
	title  = titleVar.get()
	xlabel = xLabelVar.get()
	ylabel = yLabelVar.get()

	# Backend Magic
	x, y = backend.graphList(eqn, low, high)
	# backend.graph(x, y, xlabel, ylabel, color, linestyle, title, eqn)
	backend.graph(x, y, xlabel, ylabel, 'red', '--', title, eqn)


# GUI
root = Tk()

# Label For The Title
lbl = Label(root, text='Graph Illustrator', bg='black', fg='white', font='times 30 bold')
lbl.pack(side=TOP, ipady=5, fill=X)

# Frame For Equation and Range Inputs
inputFrame = LabelFrame(root, text='Equation and Range')  
inputFrame.pack(pady=10, padx=20, expand=YES, fill=BOTH, side=TOP)


# Frame For Title and x/y - Labels
topicFrame = LabelFrame(root, text='Title and Labels')
topicFrame.pack(pady=5, padx=20, expand=YES, fill=X)


# Input Variables
eqnVar  = StringVar()
xLabel  = StringVar()
yLabel  = StringVar()
lowVar  = IntVar()
highVar = IntVar()

titleVar  = StringVar()
xLabelVar = StringVar()
yLabelVar = StringVar()

# Label Widgets
eqn      = Label(inputFrame, text="Equation f(x)", font="comicsansms 13 bold")
eqnRange = Label(inputFrame, text="Range",    font="comicsansms 13 bold")
title   = Label(topicFrame, text="Title", font="comicsansms 13 bold")
xLabel   = Label(topicFrame, text="x-Label", font="comicsansms 13 bold")
yLabel   = Label(topicFrame, text="y-Label", font="comicsansms 13 bold")


# Entry Widgets for Topic Frame
titleEntry  = ttk.Entry(topicFrame, width=30, textvar=titleVar,  font="comicsansms 13")
xLabelEntry = ttk.Entry(topicFrame, width=30, textvar=xLabelVar,  font="comicsansms 13")
yLabelEntry = ttk.Entry(topicFrame, width=30, textvar=yLabelVar,  font="comicsansms 13")


# Place the Widgets
eqn.place(x=60, y=15)
eqnRange.place(x=270, y=15)

title.grid(row=0,  column=0, padx=20, pady=(10, 0))
xLabel.grid(row=1, column=0)
yLabel.grid(row=2, column=0)

titleEntry.grid(row=0 , column=1, pady=5)
xLabelEntry.grid(row=1, column=1, pady=5)
yLabelEntry.grid(row=2, column=1, pady=5)
addCommand()
# eqnEntry  = ttk.Entry(inputFrame, width=20, textvar=eqnVar,  font="comicsansms 13")
# lowEntry  = ttk.Entry(inputFrame, width=5 , textvar=lowVar,  font="comicsansms 13")
# highEntry = ttk.Entry(inputFrame, width=5 , textvar=highVar, font="comicsansms 13")
# dashLabel = Label(inputFrame, text="-", font="comicsansms 13 bold")

# eqnEntry.place(x=20, y=38)
# lowEntry.place(x=240, y=38)
# dashLabel.place(x=295, y=38)
# highEntry.place(x=313, y=38)


# Buttons
# Add New Equation
addBtn = Button(root, text="Add Equation", bg="steelblue", fg="black", width=15, 
	font="comicsansms 10 bold", command=addCommand)
addBtn.pack(side=LEFT, padx=(20, 10), pady=10)

# Generate Graph
genBtn = Button(root, text="Generate Graph", bg="#00b72e", fg="black", width=15, 
	font="comicsansms 10 bold", command=generateCommand)
genBtn.pack(side=LEFT, padx=(20, 10), pady=10)


# GUI Config
root.title('Graph Illustrator')
root.geometry('600x500')
root.mainloop()