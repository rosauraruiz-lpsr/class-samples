import turtle

def drawRed(myTurtle):
	myTurtle.color("red")
	count = 0
	while count < 4:
		myTurtle.forward(20)
		myTurtle.right(90)
		count = count + 1

def drawBlue(myTurtle):
	number = 0
	drawRed(shawn)
	myTurtle.forward(20)
	while number < 4:
		myTurtle.color("blue")
		myTurtle.forward(20)
		myTurtle.right(90)
		number = number + 1

def drawYellow(myTurtle):
	num = 0
	drawBlue(shawn)
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
	while num < 4:
		myTurtle.color("yellow")
		myTurtle.forward(20)
		myTurtle.right(90)
		num = num + 1
def drawGreen(myTurtle):
	nums = 0
	drawYellow(shawn)
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
	while nums < 4:
		myTurtle.color("green")
		myTurtle.forward(20)
		myTurtle.right(90)
		nums = nums + 1
def multipleSquare(myTurtle):
	numb = 0
	while numb < 6:
		drawGreen(shawn)
		myTurtle.penup()
	        myTurtle.left(90)
	        myTurtle.backward(13)
	        myTurtle.left(90)
	        myTurtle.pendown()
       	 	numb = numb + 1
shawn = turtle.Turtle()
multipleSquare(shawn)
turtle.exitonclick()



















