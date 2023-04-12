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
guessed_states = []


while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_file = pandas.DataFrame(missing_states)
        new_file.to_csv("states_to_learn.csv")
        break
    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)




