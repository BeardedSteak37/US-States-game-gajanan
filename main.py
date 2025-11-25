import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)
game_on = True
score = 0
guessed_states = []

states_df = pd.read_csv("50_states.csv")

while game_on:
    answer_state = screen.textinput(title=f"{score}/50 guessed correctly", prompt="What is the state?").lower()

    if answer_state == "exit":
        break

    if states_df["state"].str.contains(answer_state, case=False, na=False).any() and answer_state not in guessed_states:
        score += 1
        guessed_states.append(answer_state)
        #store x, y of state
        row_df = states_df[states_df['state'].str.lower() == answer_state]
        x = int(row_df.iloc[0]['x'])
        y = int(row_df.iloc[0]['y'])
        # print(x)
        # print(y)
        #write onto map
        state_writer = turtle.Turtle()
        state_writer.hideturtle()
        state_writer.penup()
        state_writer.goto(x, y)
        state_writer.write(f"{answer_state.title()}")



#save non guessed states to csv
missed_states_dict = {
    "state": [],
    "x": [],
    "y": []
}

#turn state column to list
state_list = states_df.state.tolist()
for state in state_list: # add missed states to dict
    if state.lower() not in (s.lower() for s in guessed_states):
        missed_states_dict["state"].append(state)

        row_df = states_df[states_df['state'].str.lower() == state.lower()]
        if not row_df.empty:
            x = int(row_df.iloc[0]['x'])
            y = int(row_df.iloc[0]['y'])
            missed_states_dict["x"].append(x)
            missed_states_dict["y"].append(y)
        else:
            # Optional: handle no match found gracefully
            print(f"Warning: State '{state}' not found in states_df")

#turn missed_states_dict to DataFrame then csv
missed_states_df = pd.DataFrame(missed_states_dict)
missed_states_df.to_csv("missed_states.csv")