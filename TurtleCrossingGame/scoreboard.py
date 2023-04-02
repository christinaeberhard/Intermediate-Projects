from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 270)
        self.write(f"Your level: {self.user_level}", align="center", font=("Montserrat", 14, "bold"))

    def level_up(self):
        self.user_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over.", align="center", font=("Montserrat", 14, "bold"))


