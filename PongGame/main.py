import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong!")

#turning of the automation
screen.tracer(0)

# creating all necessary objects from the modules
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# game control
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    # in addition to tracer(0)
    screen.update()
    ball.move()

    # detect collision with the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect dismissing r_paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.point_for_l()

    # detect dismissing l_paddle
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.point_for_r()






screen.exitonclick()