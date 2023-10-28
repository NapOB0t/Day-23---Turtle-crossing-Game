from turtle import Screen
from Player import Player
from Car_Management import Cars
from Scoreboard import Score
from Scoreboard import LEVEL
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Mbn turtle crossing game")
screen.tracer(0)


#Player turtle movement configuration

player = Player()
screen.listen()
screen.onkey(player.up, "Up")

# Cars configuration

cars = Cars()

# Game score board

score = Score()
game_is_on = True
level = LEVEL
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car_create()
    cars.move_car()

    # Detect when player has won the level
    if player.ycor() >= 250:

       player.start_pos()
       score.levelUpdate()
       cars.accelerate()

    # Detect the player and car collision
    for x in cars.all_cars:
        if player.distance(x) <= 30:
            game_is_on = False
            score.gameover()



screen.exitonclick()
