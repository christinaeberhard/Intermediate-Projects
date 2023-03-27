import turtle as t
import random

race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: " )
colors = ["red", "orange", "brown", "green", "blue", "purple"]
y_position = [-100, -65, -30, 5, 40, 75]
turtle_list = []


for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtle_list.append(new_turtle)

if user_choice:
    race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_choice:
                print(f"You've won! The {winner_turtle} turtle won the race!")
            else:
                print(f"You lose! The {winner_turtle} turtle won the race!")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()