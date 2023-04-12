import turtle
import pandas

# create the window incl. the picture of the USA
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")

if answer in states:
    pass


