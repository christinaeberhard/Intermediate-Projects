import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# implement black screen with title
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Christinas Snake Game")

# turning off the animation
screen.tracer(0)

# create new objects from the classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# control the snake with keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    # in addition to tracer(0)
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow_snake()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()

    # detect collision with tail, starting with the 2nd segment until the end of the snake (0 would be the head)
    for segment in snake.segments[1:]:
        """ necessary because the 2nd if statement would immediately end in game over 
        because the head is less than 10 away from itself """
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
