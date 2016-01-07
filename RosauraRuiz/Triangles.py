import turtle

def drawTriangle(myTurtle):
	count = 0
	while count < 3:
		myTurtle.forward(10)
		myTurtle.right(120)
		count = count + 1
def drawMultipleTriangles(myTurtle):
	number = 0 
	while number < 4:
		myTurtle.penup()
		myTurtle.forward(20)
		myTurtle.pendown()
		drawTriangle(shawn)
		number = number + 1
def drawTriangleRows(myTurtle):
	numbers = 0
	while numbers < 3:
		myTurtle.penup()
		shawn.goto(0,0)
		myTurtle.pendown()
		drawMultipleTriangles(shawn)
		myTurtle.right(20)
		numbers = numbers + 1


def drawSide(myTurtle):
	num = 0
	while num < 2:
		drawTriangleRows(shawn)
		myTurtle.right(120)
		num = num + 1



shawn = turtle.Turtle()
drawSide(shawn)
turtle.exitonclick()
