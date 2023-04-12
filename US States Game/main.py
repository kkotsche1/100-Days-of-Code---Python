import turtle
import pandas as pd
from turtle_names import StateName
guessed_states = []
correct_guesses = 0


screen = turtle.Screen()
screen.update()
screen.title("Konstantin's States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
raw_data = pd.read_csv("50_states.csv")
state_list = raw_data["state"].to_list()

round_is_on = True
while round_is_on:

    answer_state = screen.textinput(title=f"{correct_guesses}/50 States Guessed", prompt="Please enter a State")
    answer_state = answer_state.title()



    if answer_state in state_list:
        current_state_data = raw_data[raw_data.state == answer_state]
        x_cor = int(current_state_data.x)
        y_cor = int(current_state_data.y)
        current_state = StateName(x_cor=x_cor,y_cor=y_cor,state_name=answer_state)
        guessed_states.append(answer_state)
        correct_guesses += 1
        state_list.remove(str(answer_state))
    print(state_list)
    if answer_state == "Exit":
        missing_states = pd.Series(state_list)
        missing_states.to_csv("Missing_States.csv")
        break




turtle.mainloop()