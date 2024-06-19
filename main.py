import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Monaco", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()
state_count = 0
running = True

while running:
    answer_state = screen.textinput(title=f"{state_count}/50 Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Quit":
        running = False

    if answer_state in states:
        state_count += 1
        states.remove(answer_state)
        correct_state = turtle.Turtle()
        correct_state.penup()
        correct_state.hideturtle()
        ex = float(data[data["state"] == answer_state].x.iloc[0])
        why = float(data[data["state"] == answer_state].y.iloc[0])
        correct_state.goto(ex, why)
        correct_state.write(arg=answer_state, align=ALIGNMENT, font=FONT)

        if state_count == 50:
            running = False
            congrats = turtle.Turtle()
            congrats.hideturtle()
            congrats.penup()
            congrats.goto(0, 0)
            congrats.write(arg="Congratulations! You win!", align=ALIGNMENT, font=("Monaco", 24, "bold"))

missed_states = pandas.DataFrame(states)
missed_states.to_csv("states_to_learn.csv")
