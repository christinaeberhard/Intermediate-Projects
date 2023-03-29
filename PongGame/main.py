import turtle as t

from pygments.lexers import go

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong!")

#turning of the automation
screen.tracer(0)

paddle = t.Turtle()
paddle.shape("square")
paddle.color("white")
""" default size of a square turtle is 20 x 20 (20 =1), so we need 5 to get 100 """
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    # in addition to tracer(0)
    screen.update()




screen.exitonclick()