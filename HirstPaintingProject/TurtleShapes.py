from turtle import *
import random

noah = Turtle()
noah.color("DarkSalmon")

colors = ["DarkGoldenrod", "DarkSalmon", "DarkSlateGrey", "DarkSeaGreen", "comsilk4", "DarkGreen", "coral4", "burlywood4"]

def draw_shapes(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        noah.forward(100)
        noah.right(angle)

for n in range (3, 11):
    noah.color(random.choice(colors))
    draw_shapes(n)


screen = Screen()
screen.exitonclick()
