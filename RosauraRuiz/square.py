# square.py

import turtle

# make our turtle
abc = turtle.Turtle()
# makes the addition sign red
abc.color("red")
# abc makes a addition sign
abc.shape("turtle")
lines = 0 
while lines < 9:
	abc.forward(100)
	abc.backward(50)
	abc.right(40)
	lines = lines + 1
	abc.shape("arrow")
turtle.exitonclick()
