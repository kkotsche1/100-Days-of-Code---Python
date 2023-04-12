from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from ScoreBoard import ScoreBoard
FONT = ("arial", 10, "bold")


game_is_on = True
high_score = 0
while game_is_on:

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Konstantin's Snake Game")
    screen.tracer(0)
    scoreboard = ScoreBoard()
    snake = Snake()
    food = Food()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    highscore = Turtle()
    highscore.clear()
    highscore.color("white")
    highscore.penup()
    highscore.hideturtle()
    highscore.setposition(x=100, y=285)
    highscore.write(f"High Score: {high_score}", False, align="center", font=FONT)
    round_is_on = True
    screen.update()
    while round_is_on:
        screen.update()
        time.sleep(0.1)
        screen.listen()
        snake.move_forward()


    # Detecting collision with food

        if snake.head.distance(food) < 17:
            food.move()
            scoreboard.increase_score()
            snake.extend()


    # Detecting collision with wall

        if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() < -290 or snake.head.ycor() >290:
            game_score = scoreboard.game_over()
            if game_score > high_score:
                high_score = game_score
            screen.clear()
            round_is_on = False

    # Detecting collision with snake tail

        for segment in snake.segments[2:]:
            if snake.head.distance(segment.pos()) < 1:
                if game_score > high_score:
                    high_score = game_score
                scoreboard.game_over()
                screen.clear()
                round_is_on = False













screen.exitonclick()