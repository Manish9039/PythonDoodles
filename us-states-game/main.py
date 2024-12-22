import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

correct_count = 0
correct_guess = []

while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{correct_count}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in states if state not in correct_guess]
        # for state in states:
        #     if state not in correct_guess:
        #         states_to_learn.append(state)
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("States_to_learn.csv")
        break

    if answer_state in states:
        correct_count += 1
        correct_guess.append(answer_state)
        row = data[data.state == answer_state]
        timmy = turtle.Turtle()
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(int(row.x), int(row.y))
        timmy.write(answer_state)


screen.exitonclick()

