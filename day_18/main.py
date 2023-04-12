from turtle import Turtle
from turtle import Screen
screen = Screen()
screen.colormode(255)


tim = Turtle()
Turtle.colormode = 255
tim.shape("turtle")
tim.color("darkorchid4")
tim.pensize(10)
tim.speed = 8
from random import randint



random_runs = 0
while random_runs < 15:

    rgb_x = randint(0, 255)
    rgb_y = randint(0, 255)
    rgb_z = randint(0, 255)
    tim.pencolor(rgb_x, rgb_y, rgb_z)
    tim.forward(100)
    heading = randint(1,101)
    if heading < 26:
        tim.right(90)
    elif heading < 51:
        tim.left(90)
    elif heading < 76:
        tim.right(90)
    else:
        tim.left(90)

    random_runs += 1
















screen.exitonclick()
