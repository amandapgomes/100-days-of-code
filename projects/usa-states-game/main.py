import turtle
import pandas

screen = turtle.Screen()
screen.title("U. S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_names = data["state"].to_list()

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guessed_list = []
while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 - Guess a State", prompt="What's another state's "
                                                                                            "name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in states_names if state not in guessed_list]
        missing_states = pandas.DataFrame(states_to_learn)
        missing_states.to_csv("missing_states.csv")
        break

    if answer_state in states_names:
        guessed_list.append(answer_state)
        names_writer = turtle.Turtle()
        names_writer.hideturtle()
        names_writer.penup()
        state_data = data[data.state == answer_state]
        names_writer.goto(int(state_data.x), int(state_data.y))
        names_writer.write(f"{state_data.state.item()}", align="center", font=("Arial", 8, "normal"))



