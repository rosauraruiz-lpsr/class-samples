import turtle

def makeSquare(myTurtle, side):
        myTurtle.forward(side)
        myTurtle.left(60)
        myTurtle.forward(side)
        myTurtle.left(60)
        myTurtle.forward(side)

squeak = turtle.Turtle()

length = 100
while length > 0:
        makeSquare(squeak, length)
        squeak.right(5)
        length = length - 1


turtle.exitonclick()
