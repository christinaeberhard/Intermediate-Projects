import turtle as t
from snake import Snake
import time

# implement black screen with title
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Christinas Snake Game")
screen.tracer(0)

snake = Snake()

# control the snake with keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move the snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
