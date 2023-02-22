from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 500)
bet = screen.textinput(title="What is your bet", prompt="Which turtle will win ? Enter a color from VIBGYOR")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_cordinates = [-170, -140, -110, -80, -50, -20, 10]
all_turtle = []
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-238, y_cordinates[turtle_index])
    all_turtle.append(new_turtle)


if bet:
    game_on = True

while game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 238:
            game_on = False
            winner = turtle.color()
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if winner[0] == bet.lower():
    print(f"You've won the bet {bet.lower} wins!!!")
else:
    print(f"You lose, {winner[0]} turtle wins!!!")

screen.exitonclick()
