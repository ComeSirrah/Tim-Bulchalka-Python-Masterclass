from turtle import *
# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()

import turtle
from math import radians, cos


def square(length: int) -> None:
    """Draws a square of length `length`"""
    for side in range(4):
        forward(length)
        right(90)


def encircled_square(length: int) -> None:
    """Draws a square of length `length`,
    then encloses it in a circle.
    """
    square(length)
    angle = radians(45)
    radius = length * cos(angle)
    right(135)
    circle(radius)
    left(135)
    print(f'Inside function, namespace is: {dir()}')
    print(f'locals: {locals()}')


# encircled_square(300)
turtle.speed('fast')
Screen().tracer(0)  # disable  visual updates to the drawing as it processes
for s in range(72):
    encircled_square(120)
    left(5)

turtle.done()

print(dir())
g = globals()
print(g['square'])

print(dir(__builtins__))