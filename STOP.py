#CS175

#Arnab Sahoo

#STOP


import turtle

import math

 

# Named constants

WINDOW_WIDTH = 400

WINDOW_HEIGHT = 400

ANIMATION_SPEED = 0

NUM_SIDES = 8

LENGTH = 100

ANGLE = 45

TEXT_X = -10

TEXT_Y = -30

GAP = 20

 

# Size the window.

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

 

# Calculate the diameter of the octagon

s = LENGTH

x = s / math.sqrt(2)

diameter = s + (2 * x)

 

# Initialize the turtle.

t = turtle.Turtle()

t.shape('turtle')

t.speed(ANIMATION_SPEED)

 

# Function to draw an octagon

def draw_octagon(turtle, start_pos, side_length, color, fill=False):

    turtle.penup()

    turtle.goto(start_pos)

    turtle.pendown()

    turtle.color(color)

    if fill:

        turtle.begin_fill()

    for _ in range(NUM_SIDES):

        turtle.forward(side_length)

        turtle.right(ANGLE)

    if fill:

        turtle.end_fill()

 

# Draw the outer red octagon

t.pensize(10)  # Make the pen thicker

draw_octagon(t, (-75, 170), diameter/2 + GAP, "red")

 

t.pensize(1)  # Reset the pen size

 

# Draw the inner red octagon

draw_octagon(t, (-65, 150), diameter/2, "red", fill=True)

 

# Write 'STOP' in white color at the center of the inner octagon

t.penup()

t.goto(TEXT_X, TEXT_Y)

t.color('white')

t.write('STOP', align='center', font=("Arial", 50, "bold"))

 

t.hideturtle()

turtle.done()

