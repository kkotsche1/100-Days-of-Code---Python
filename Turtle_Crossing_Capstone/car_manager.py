COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 2
from turtle import Turtle
from random import randint

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.move_increment = STARTING_MOVE_DISTANCE
        self.shape("square")
        self.car_set = []
        x=0
        while x<7:
            self.create_car()
            print(self.car_set)
            x += 1


    def create_car(self):
        car = Turtle()
        car.color("black")
        car.penup()
        car.shape("square")
        car.color(COLORS[randint(0,5)])
        car.setheading(180)
        x_position = randint(200,1000)
        y_position = randint(-220,210)
        car.setposition(x=x_position, y=y_position)
        car.shapesize(stretch_len=2.5)
        self.car_set.append(car)

    def move_forward(self):
        for vehicle in self.car_set:
            vehicle.forward(self.move_increment)

    def increase_speed(self):
        self.move_increment += MOVE_INCREMENT

    def reset_speed(self):
        self.move_increment = STARTING_MOVE_DISTANCE