from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.draw_finish_line()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()
        self.move_distance=MOVE_DISTANCE

    def move_forward(self):
        new_y = self.ycor() + self.move_distance
        self.sety(new_y)

    def move_backward(self):
        new_y = self.ycor() - self.move_distance
        self.sety(new_y)

    def move_right(self):
        new_x = self.xcor() + self.move_distance
        self.setx(new_x)

    def move_left(self):
        new_x = self.xcor() - self.move_distance
        self.setx(new_x)

    def draw_finish_line(self):
        self.penup()
        self.goto(x=-350, y=230)
        self.pensize(10)
        self.setheading(0)
        self.pendown()
        self.color("green")
        self.hideturtle()
        self.goto(x=470, y=230)
        self.penup()

    def return_home(self):
        self.goto(STARTING_POSITION)
