# import all necessary modules
from colorgram import color_list
import turtle as t
import random as rd

# set colormode and create an object (not visible and fast)
t.colormode(255)
noah = t.Turtle()
noah.speed("fastest")
noah.penup()
noah.hideturtle()

# set starting point
noah.setheading(225)
noah.forward(300)
noah.setheading(0)
number_of_dots = 100

# start painting
for dots in range(1, number_of_dots + 1):
    noah.dot(20, rd.choice(color_list))
    noah.forward(50)

    if dots % 10 == 0:
        noah.setheading(90)
        noah.forward(50)
        noah.setheading(180)
        noah.forward(500)
        noah.setheading(0)


screen = t.Screen()
screen.exitonclick()