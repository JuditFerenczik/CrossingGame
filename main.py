import time
from turtle import Screen
from player import Player
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up,"Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()
    for enemy in car_manager.enemies:
        if enemy.distance(player) < 20:
            game_is_on = False
            scoreboard.theend()

    if player.ycor() > 280:
        player.start()
        car_manager.enemies_speed += MOVE_INCREMENT
        scoreboard.level += 1
        scoreboard.update()



screen.exitonclick()


