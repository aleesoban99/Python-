import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. STATE GAME")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",prompt="What's another state name?").title()

    if answer_state =="Exit":
        missing_states=[]
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        print(missing_states)
        break

    answer_state = answer_state.title()
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]

        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)