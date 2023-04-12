from turtle import Screen, Turtle
from user_paddle import Paddle
from cpu_paddle import CPU_Paddle
from Scoreboard import ScoreBoard
from ball import Ball
from center_line import CenterLine
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Konstantin's Pong Game")
screen.tracer(0)
screen.listen()

user_score = ScoreBoard("user")
cpu_score = ScoreBoard("cpu")

centerline = CenterLine()
user_paddle = Paddle()
cpu_paddle = CPU_Paddle()
screen.update()
screen.onkeypress(user_paddle.up, "Up")
screen.onkeypress(user_paddle.down, "Down")

game_is_on = True

while game_is_on:
    round_is_on = True
    ball = Ball()
    while round_is_on:
        screen.update()
        time.sleep(0.001)
        cpu_paddle.move_forward()
        cpu_paddle.reverse_paddle()
        user_paddle.reverse_paddle()
        ball.move_forward()
        if ball.ycor() > 250:
            ball.change_direction()
        if ball.ycor() < -250:
            ball.change_direction()

        for segment in user_paddle.segments:
            if segment.distance(ball) < 15:
                ball.bounce_off_paddle()
            if segment.distance(ball) < 15:
                ball.bounce_off_paddle()

        for segment in cpu_paddle.segments:
            if segment.distance(ball) < 15:
                ball.bounce_off_paddle()
            if segment.distance(ball) < 15:
                ball.bounce_off_paddle()

        if ball.xcor() < -375:
            cpu_score.increase_score()
            ball.hideturtle()
            round_is_on = False
        if ball.xcor() > 375:
            user_score.increase_score()
            ball.hideturtle()
            round_is_on = False


screen.exitonclick()