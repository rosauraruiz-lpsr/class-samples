import random
import turtle

Rturtle = turtle.Turtle()

number = 50
length = 10
color = ['brown','purple','orange','red','pink','green','blue']

while number > 0:
	Rturtle.color(random.choice(color))
	Rturtle.left(90)
	Rturtle.forward(length)
	Rturtle.right(90)
	Rturtle.left(20)	
	Rturtle.forward(length)

	number = number - 1
	length = length - 1

turtle.exitonclick()
