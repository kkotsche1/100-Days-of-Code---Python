from turtle import Turtle, Screen
import time
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [0, -20, -40]

class Snake:

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]


    def createsnake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def move_forward(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            print()
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up (self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setx(position)
        self.segments.append(new_segment)


    def extend(self):
        last_position = self.segments[len(self.segments)-1].pos()
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(last_position)
        self.segments.append(new_segment)
