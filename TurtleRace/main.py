from turtle import Turtle, Screen
from random import choice, randint



screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_speeds = [0,1,2,3,4,5,6,7,8,9,10]
user_choice = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter one of the"
                                                             "following colors: red, orange, yellow, green, blue, or purple")


turtles = []

for current_color in colors:
    tim = Turtle(shape="turtle")
    tim.color(current_color)
    tim.penup()
    turtles.append(tim)

y_coordinate = -125

for turtle in turtles:
    turtle.goto(x=-230, y=y_coordinate)
    y_coordinate += 50

if user_choice:
    is_race_on = True

is_race_on = True
winning_turtle = ()
while is_race_on:
    for turtle in turtles:
        random_distance = randint(10, 20)
        turtle.forward(random_distance)
        if turtle.xcor() > 150:
            winning_turtle = turtle.color()
            is_race_on = False

winning_color = winning_turtle[0]


if winning_color == user_choice:
    print(f"You chose correctly, the {winning_color} turtle won :)")
else:
    print(f"You lose, the {winning_color} turtle won! Better luck next time :) ")







screen.exitonclick()
