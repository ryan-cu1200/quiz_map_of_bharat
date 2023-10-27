import pandas as pd
import turtle

screen = turtle.Screen()

screen.setup(600, 600)
df = pd.read_csv("bharat_all_state.csv")
states = df.states.to_list()

user_input_states = []
img = "map_of_bharat.gif"
screen.addshape(img)
turtle.shape(img)

chances = 0
while chances < 30:
    user_choice = screen.textinput(f"Bharat States! {chances}/30", prompt="Type the name of all states").title()
    if user_choice in states:
        state_data = df[df["states"] == user_choice]
        user_input_states.append(user_choice)
        bharat_map = turtle.Turtle()
        bharat_map.penup()
        bharat_map.goto(int(state_data.x_location), int(state_data.y_location))
        bharat_map.write(user_choice)
        chances += 1
    elif user_choice not in states:
        user_input_states.append(user_choice)
        chances += 1
    if user_choice == "Exit":
        exit()
dff = pd.DataFrame(user_input_states)
dff.to_csv("user_enter_states.csv")

screen.mainloop()

