from turtle import Turtle
FONT = ("arial", 10, "bold")

class StateName(Turtle):

    def __init__(self, x_cor, y_cor, state_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x=x_cor, y=y_cor)
        self.write(arg=state_name, move=False, align="center", font=FONT)
