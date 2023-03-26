import turtle as t
import random

noah = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

moving = [0, 90, 180, 360]
noah.pensize(10)

for n in range(0, 200):
    noah.forward(25)
    noah.color(random_color())
    noah.setheading(random.choice(moving))


screen = Screen()
screen.exitonclick()