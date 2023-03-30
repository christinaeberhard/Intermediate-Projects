from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # reverse vertical direction by multiplying with -1 (10 -> -10)
        self.y_move *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        # reverse horizontal direction by multiplying with -1 (10 -> -10)
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset(self):
        """ resets the ball back in the center and start moving in the opposite direction """
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()