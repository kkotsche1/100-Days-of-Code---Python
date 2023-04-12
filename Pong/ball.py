from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.color("green")
        self.speed("slow")
        x = random.randint(0,1000)
        #if x % 2 == 0:
         #   self.setheading(random.randint(-60,60))
        #else:
        self.setheading(random.randint(120, 240))

    def move_forward(self):
        self.forward(1)

    def change_direction(self):
        ty = self.ycor()


        if ty < 0:
            angleCurr = self.heading()
            if (270>angleCurr>180):
                self.right(90)
            else:
                self.left(90)

        if ty > 0:
            angleCurr = self.heading()
            if (0<angleCurr<90):
                self.right(90)
            else:
                self.left(90)

    def bounce_off_paddle(self):
        tx = self.xcor()

        if tx < 0:
            angleCurr = self.heading()
            if 90 < angleCurr < 180:
                self.right(90)
            else:
                self.left(90)
        else:
            angleCurr = self.heading()
            if 90 < angleCurr < 180:
                self.left(90)
            else:
                self.right(90)
