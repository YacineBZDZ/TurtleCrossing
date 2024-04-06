import time
from turtle import Screen

import player as p
from player import Player
from car_manager import CarManager
import car_manager as c
import scoreboard  as  s

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = p.Player()
c1 = c.CarManager()
lvl = s.Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    lvl.update_scoreboard()
    c1.create_cars()
    c1.move()
    for car in c1.cars :
        if player1.distance(car) < 25:
            game_is_on = False
            lvl.gameover()
    if player1.ycor() > 280:
        lvl.scoreincrease()
        player1.resetPoistion()
        c1.UpLvl()

    if lvl.score == 1:
        screen.bgcolor("red")
    elif lvl.score == 2 :
        screen.bgcolor("blue")
    screen.listen()
    screen.onkey(player1.Up,"Up")


screen.exitonclick()