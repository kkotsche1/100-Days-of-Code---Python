from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
import time

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score},    High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def check_high_score(self):
        with open("data.txt") as file:
            data_high_score = int(file.read())
        print(data_high_score)
        if data_high_score >= int(self.highscore):
            self.highscore = data_high_score
        else:
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
