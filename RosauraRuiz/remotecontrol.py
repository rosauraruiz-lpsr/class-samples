import turtle
from Tkinter import *
import random

def octagon(myTurtle):
	side_count = 0
	while side_count < 8:
		myTurtle.forward(45)
		myTurtle.right(45)
		side_count = side_count + 1
# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)
# create our turtle
shawn = turtle.Turtle()
ccc= ['purple','orange','blue','pink','red']
# make some simple buttons
fwd = Button(frame, text = 'fwd', command=lambda: shawn.forward(50))
left = Button(frame, text = 'left', command=lambda: shawn.left(90))
right = Button(frame, text = 'right', command=lambda: shawn.right(90))
penup = Button(frame, text= 'penup', command=lambda: shawn.penup())
pendown = Button(frame, text = 'pendown', command=lambda: shawn.pendown())
color = Button(frame, text = 'random color', command=lambda: shawn.color(random.choice(ccc)))
octagonButton = Button(frame, text = 'octagon', command=lambda: octagon(shawn))
# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
color.pack(side=LEFT)
octagonButton.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
