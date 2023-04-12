import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player
from random import randint

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Konstantin's Turtle Game")
screen.listen()
scoreboard = Scoreboard()
scoreboard.initialize_score()
carmanager = CarManager()
player = Player()
screen.onkey(fun=player.move_forward, key="Up")
screen.onkey(fun=player.move_backward, key="Down")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")
screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.01)

    for car in carmanager.car_set:
        if car.xcor() < -300:
            car.setx(350)
            car.sety(randint(-225,210))
        if car.xcor()-35 < player.xcor() < car.xcor() +35 and car.ycor()-25 < player.ycor() < car.ycor()+25:
            scoreboard.game_over()
            scoreboard.reset_score()
            player.return_home()
            carmanager.reset_speed()


    carmanager.move_forward()
    if player.ycor() > 230:
        scoreboard.increase_score()
        player.return_home()
        carmanager.increase_speed()


screen.exitonclick()
