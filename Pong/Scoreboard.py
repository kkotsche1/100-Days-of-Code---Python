from turtle import Turtle

FONT = ("arial", 30, "bold")
GAMEOVERFONT = ("arial", 25, "bold")


class ScoreBoard(Turtle):

    def __init__(self, identifier):
        super().__init__()
        self.color("white")
        self.current_score = 0
        self.penup()
        self.hideturtle()
        if identifier == "user":
            self.setposition(x = -200, y =230)
        if identifier == "cpu":
            self.setposition(x = 200, y =230)
        self.write(f"{self.current_score}", False, align="center", font= FONT)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"{self.current_score}", False, align="center", font= FONT)

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write(f"Game Over!", False, align="center", font=GAMEOVERFONT)
