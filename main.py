import turtle
from turtle import Turtle, Screen
import pandas

# Set up the screen and turtle
screen = Screen()
ammu = Turtle()
screen.title("U.S States Game")

# Load the image of blank states
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# Read the data containing state information
data = pandas.read_csv("50_states.csv")

# Initialize game variables
game_is_on = True
already_guessed = []
score = 0

# Main game loop
while game_is_on:
    # Get user input for state name
    user_input = screen.textinput(title=f"{score}/50 State Names", prompt="What's another state name?").title()

    # Check if the game should end
    if score == 50 or str(user_input) == "Exit":
        game_is_on = False

    # Check if the state has already been guessed
    elif str(user_input) in already_guessed:
        score = score

    # Check if the input matches a state in the dataset
    elif str(user_input) in str(data["state"]):
        already_guessed.append(str(user_input))
        ammu.hideturtle()
        ammu.penup()
        row_data = data[data["state"] == user_input]
        x_value = int(row_data.x.iloc[0])
        y_value = int(row_data.y.iloc[0])
        ammu.goto(x=int(x_value), y=int(y_value))
        ammu.write(f"{user_input}", align="center", font=("Courier", 8, "normal"))
        score += 1

# Prepare data for saving
original_data = data["state"].tolist()
a = set(original_data)
b = set(already_guessed)
c = list(a.symmetric_difference(b))

# Create a DataFrame from the differences
new_data = pandas.DataFrame(c)

# Save the differences to a CSV file
new_data.to_csv("./learn_states_name.csv")
