import turtle as t
import random

noah = t.Turtle()
t.colormode(255)
noah.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

def spirograph(size_of_gap):
    for n in range(int(360 / size_of_gap)):
        noah.color(random_color())
        noah.circle(100)
        noah.right(size_of_gap)


spirograph(5)

screen = t.Screen()
screen.exitonclick()

