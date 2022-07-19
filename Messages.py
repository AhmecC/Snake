from turtle import Turtle
import time
from Scoreboard import Scoreboard

class Message(Turtle):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.end()

    def end(self):
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.ht()
        self.clear()
        self.write(f"GAME OVER", True, align="center", font=("Calibri", 30, "normal"))


