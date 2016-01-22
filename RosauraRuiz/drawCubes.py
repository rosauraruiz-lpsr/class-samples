import turtle
# This function makes a rhombus 
def MakesRhombus(myTurtle):
	count = 0
	myTurtle.right(30)
	while count < 2:
		myTurtle.left(60)
		myTurtle.forward(40)
		myTurtle.left(120)
		myTurtle.forward(40)
		count = count + 1	
# This function makes another rhombus attatched to the first rhombus, the color of this side is red
def drawSideOfRhombus(myTurtle):
	MakesRhombus(myTurtle)
	myTurtle.left(150)
	shawn.fillcolor("red")
	shawn.begin_fill()
	MakesRhombus(myTurtle)
	shawn.end_fill()
# This function attaches another rhombus this side is pink , now it looks like a cube.
def drawOtherSide(myTurtle):
	drawSideOfRhombus(myTurtle)
	myTurtle.left(150)
	myTurtle.fillcolor("pink")
	myTurtle.begin_fill()
	MakesRhombus(myTurtle)
	myTurtle.end_fill()
# This function is a function for the cube
def drawCube(myTurtle):
	drawOtherSide(myTurtle)
# This function moves the arrow in order to make a row 
def MoveArrow(myTurtle):
	myTurtle.right(60)
	myTurtle.forward(40)
	myTurtle.left(60)
	myTurtle.penup()
	myTurtle.forward(40)
	myTurtle.right(210)
	myTurtle.pendown()
# This function draws the first row of cubes 
def drawFirstRow(myTurtle):
	number = 0
	while number < 2:
		drawCube(myTurtle)
		MoveArrow(myTurtle)
		drawCube(myTurtle)
		MoveArrow(myTurtle)
		number = number + 1
# This function draws the second row of cubes
def drawSecondRow(myTurtle):
	drawFirstRow(myTurtle)
	myTurtle.penup()
	myTurtle.goto(0,0)
	myTurtle.right(90)
	myTurtle.forward(60)
	myTurtle.left(90)
	myTurtle.backward(35)
	myTurtle.pendown()
	drawFirstRow(myTurtle)	
# This function draws the third row of cubes
def drawThirdRow(myTurtle):
	drawSecondRow(myTurtle)
	myTurtle.penup()
	myTurtle.goto(0,0)
	myTurtle.right(90)
	myTurtle.forward(120)
	myTurtle.left(90)
	myTurtle.backward(70)
	myTurtle.pendown()
	drawFirstRow(myTurtle)


shawn = turtle.Turtle()
drawThirdRow(shawn)
turtle.exitonclick()
