# Modules
import matplotlib.pyplot as plt
from tkinter import *


# Functions
def graph(x, y, xlabel, ylabel, color, linestyle, title, eqn):
	plt.figure(dpi=150)
	plt.style.use('ggplot')
	plt.title(title, fontdict={'fontname':'Comic Sans MS', 'fontweight':'bold', 'fontsize':20})

	plt.plot(x, y, color=color, linestyle=linestyle, label='y = ' + eqn, marker='*')
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	plt.legend()
	plt.show()


def graphList(eqn, low, high):
	x = []
	y = []
	for number in range(low, high+1):
		x.append(number)
		y.append( eval( eqn.replace("x", str(number)) ) )
	print(x, y)
	return x, y


class Equations:

	def __init__(self, inputFrame, eqn, low, high, y):
		self.inputFrame = inputFrame
		self.eqnEntry   = eqn					
		self.lowEntry   = low									
		self.highEntry  = high
		self.yaxis      = y

		eqnEntry  = ttk.Entry(inputFrame, width=20, textvar=eqn,  font="comicsansms 13")
		lowEntry  = ttk.Entry(inputFrame, width=5 , textvar=low,  font="comicsansms 13")
		highEntry = ttk.Entry(inputFrame, width=5 , textvar=high, font="comicsansms 13")
		dashLabel = Label(inputFrame, text="-", font="comicsansms 13 bold")


	def hello(self):
		self.eqnEntry.place(x=20, y=y)
		self.lowEntry.place(x=240, y=y)
		# self.dashLabel.place(x=295, y=y)
		self.highEntry.place(x=313, y=y)


if __name__ == '__main__':
	eqn  = str(input('Enter the equation f(x): '))
	low  = int(input('Enter low point: '))
	high = int(input('Enter high point: '))

	x, y = graphList(eqn, low, high)
	
	xlabel    = "X-axis"
	ylabel    = "Y-axis"
	color     = 'red'
	linestyle = '--'
	title     = 'Line Graph'
	graph(x, y, xlabel, ylabel, color, linestyle, title, eqn)
