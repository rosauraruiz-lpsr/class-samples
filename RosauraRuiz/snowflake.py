# myFractalTemplate.py
 
import turtle
 
def makeHexagon(myTurtle, side):
        myTurtle.color("burlywood1")
        myTurtle.forward(side)
	myTurtle.color("black")
        myTurtle.right(60)
        myTurtle.forward(side)
        myTurtle.right(60)
        myTurtle.forward(side)
        myTurtle.right(60)
        myTurtle.forward(side)
        myTurtle.right(60)
        myTurtle.forward(side)
        myTurtle.right(60) 
        myTurtle.forward(side)
    
squeak = turtle.Turtle()
 
# squeak makes squares centered at the same point
# but going in a slightly rotated position with each loop
# and with a slightly smaller side length each time
length = 100
while length > 0:
        makeHexagon(squeak, length)
# rotate and make the sides shorter
        squeak.right(5)
        length = length - 1
 
# wait to exit until I've clicked
turtle.exitonclick()


