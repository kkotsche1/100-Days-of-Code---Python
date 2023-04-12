from turtle import Turtle

FONT = ("arial", 10, "bold")
GAMEOVERFONT = ("arial", 25, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.current_score = 0
        self.penup()
        self.hideturtle()
        self.highscore = 0
        self.setposition(x = -100, y =285)
        self.write(f"Current Score: {self.current_score}", False, align="center", font= FONT)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Current Score: {self.current_score}", False, align="center", font= FONT)

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write(f"Game Over!", False, align="center", font=GAMEOVERFONT)
        return self.current_score

    def update_high_score(self):
        if self.current_score > self.highscore:
            self.highscore = self.current_score
        self.clear()
        self.write(f"Current Score: {self.current_score}   High Score: {self.highscore}", False, align="center",
                   font=FONT)