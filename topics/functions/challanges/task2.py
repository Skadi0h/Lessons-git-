"""
Create functions to draw Turtle figures for:
 - triangle
 - circle
 - hexagon
 - n-gonal regular polygon

Note:
    Regular pylygon
    (Правильный многоугольник)
    https://en.wikipedia.org/wiki/Regular_polygon


Hint:

def draw_square(side_length: int) -> None:
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

draw_square(100)
"""

import turtle  # <- get functions and classes from turtle lib


# write code here
def draw_triangle(side_length: int) -> None:
    for _ in range(3):
        turtle.forward(side_length)
        turtle.right(120)


def draw_circle(radius: int) -> None:
    turtle.circle(radius)


def draw_hexagon(side_length: int) -> None:
    for _ in range(6):
        turtle.forward(side_length)
        turtle.right(60)


def draw_polygon(n: int, side_length: int) -> None:
    if n == 0:
        raise ZeroDivisionError('Nun of sides cannot be 0')

    angle = 360 / n
    for _ in range(n):
        turtle.forward(side_length)
        turtle.right(angle)

#
# draw_triangle(100)
# draw_circle(100)
# draw_hexagon(100)
# draw_ngonal_polygon(n=8, side_length=100)

# to wait users' click instead of immediately exit, don't touch it pls
turtle.Screen().exitonclick()
