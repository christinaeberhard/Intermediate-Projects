import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("DarkSalmon")
screen.tracer(0)
screen.title("Crossing Turtles!")

# create all necessary objects
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

# game control
screen.listen()
screen.onkey(player.go_up, "Up")

# game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # detect if turtle is arriving top
    if player.ycor() > 300:
        scoreboard.level_up()
        player.reset()




screen.exitonclick()
