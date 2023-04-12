from turtle import Turtle
import random


class CenterLine(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(7)
        self.speed("fastest")
        self.setpos(0, -325)
        self.setheading(90)

        x = 0

        while x < 20:
            self.forward(25)
            self.pendown()
            self.forward(25)
            self.penup()
            x += 1