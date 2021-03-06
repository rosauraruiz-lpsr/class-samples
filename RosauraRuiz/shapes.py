# shapeDrawer.py
# draws user-input shapes in random places on the screen
# with random sizes and colors
# bring in the packages of functions we need
import random
import turtle
 
# -------- functions start here ----------------
 
def regular_triangle(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        myTurtle.color(random.choice(color))
        side_count = 0
        while side_count < 3:
                myTurtle.forward(side)
                myTurtle.right(120)
                side_count = side_count + 1
 
def regular_square(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.color(random.choice(color))
        myTurtle.pendown()
        side_count = 0
        while side_count < 4:
                myTurtle.forward(side)
                myTurtle.right(90)
                side_count = side_count + 1
 
def regular_pentagon(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.color(random.choice(color))
        myTurtle.pendown()
        side_count = 0
        while side_count < 5:
                myTurtle.forward(side)
                myTurtle.left(72)
                side_count = side_count + 1
 
def regular_hexagon(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        myTurtle.color(random.choice(color))
        side_count = 0 
        while side_count < 6:
                myTurtle.forward(side)
                myTurtle.right(60)
                side_count = side_count + 1
def regular_octagon(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        myTurtle.color(random.choice(color))
        side_count = 0
        while side_count < 8:
                myTurtle.forward(side)
                myTurtle.right(45)
                side_count = side_count + 1
 
def circle(myTurtle, x, y, radius):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        myTurtle.color(random.choice(color))
        myTurtle.circle(radius)
def smiley(myTurtle, x, y, radius):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        myTurtle.color(random.choice(color))
        myTurtle.right(90)
        myTurtle.forward(45)
        myTurtle.right(90)
        myTurtle.forward(85)
        myTurtle.right(90)
        myTurtle.forward(45)
        myTurtle.penup()
        myTurtle.forward(25)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.pendown()
        myTurtle.circle(25)
        myTurtle.penup()
        myTurtle.forward(60)
        myTurtle.pendown()
        myTurtle.circle(25)
# -------- execution starts here ----------------
 
print("Welcome to the random shape drawer!")
print("You choose the shapes, and we choose the position, color, and size.")
 
squirt = turtle.Turtle()
 
shape = ""
while shape != "exit":
        print("Enter a shape - your choices are triangle, square, smiley, pentagon, hexagon, octagon, and circle.")
        print("If you're done making shapes, just type 'exit'.")
        shape = raw_input()
 
        randx = random.randint(-200,200)
        randy = random.randint(-200,200)
        randside = random.randint(5,100)
        color = ['red','green','blue','purple','pink','brown','navy','orange']
        if shape == 'triangle':
                regular_triangle(squirt, randx, randy, randside)
        elif shape == 'square':
                regular_square(squirt, randx, randy, randside)
        elif shape == 'pentagon':
                regular_pentagon(squirt, randx, randy, randside)
        elif shape == 'hexagon':
                regular_hexagon(squirt, randx, randy, randside)
        elif shape == 'octagon':
                regular_octagon(squirt, randx, randy, randside)
        elif shape == 'circle':
                circle(squirt, randx, randy, randside)
        elif shape == 'smiley':
                smiley(squirt, randx, randy, randside)


