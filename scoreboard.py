from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270,270)
        self.update()

    def update(self):
        self.clear()
        self.write("Your level is {}".format(self.level),align="left", font=FONT)

    def theend(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write("You died :( Your level was {}".format(self.level), align="center", font=FONT)

