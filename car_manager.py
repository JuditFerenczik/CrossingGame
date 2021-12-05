import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.enemies_speed = STARTING_MOVE_DISTANCE
    def create(self):
        iscreate = random.randint(1,7)
        if iscreate == 6:
            enemy = Turtle()
            enemy.shape("square")
            enemy.color(random.choice(COLORS))
            enemy.shapesize(stretch_len=2,stretch_wid=1)
            enemy.penup()
            y_coord = random.randint(0,21) * 25 -250
            enemy.goto(300,y_coord)
            enemy.setheading(180)
            self.enemies.append(enemy)

    def move(self):
        for enemy in self.enemies:
            enemy.forward(self.enemies_speed)





