import turtle


def draw_circle(distance: int) -> None:
    for _ in range(30):
        turtle.right(100)
        turtle.forward(distance)


def draw_square(distance: int) -> None:
    """
    Task 8
    Draw square
    Investigate code of draw_circle
    """
    # write code here
    for _ in range(4):
        turtle.right(90)
        turtle.forward(distance)


draw_circle(100)
while True:
    ...
# draw_square(50)
