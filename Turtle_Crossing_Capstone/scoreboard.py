FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 25, "bold")
from turtle import Turtle
import time

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=-150, y=250)
        self.color("black")

    def initialize_score(self):
        self.clear()
        self.write(f"Current Score: {self.score}", False, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.initialize_score()

    def reset_score(self):
        self.score = 0
        self.initialize_score()

    def game_over(self):
        self.clear()
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.color("black")
        game_over.write(f"Game Over, you suck!", False, align="center", font=GAME_OVER_FONT)
        time.sleep(2)
        game_over.clear()
