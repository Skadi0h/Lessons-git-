import turtle


def draw_circle(distance: int) -> None:
    for _ in range(360):
        turtle.right(1)
        turtle.forward(distance)


def draw_square(distance: int) -> None:
    """
    Task 8
    Draw square
    Investigate code of draw_circle
    """
    # write code here
    ...


draw_circle(5)
draw_square(5)
