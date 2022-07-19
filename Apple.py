from turtle import Turtle
import random

class Apple(Turtle):
    def __init__(self):
        self.cords = ()
        self.apples = []
        self.create_apple()

    def create_apple(self):
        x = random.choice(range(-280, 280, 20))
        y = random.choice(range(-280, 280, 20))
        self.cords = (x, y)
        apple = Turtle(shape="circle")
        apple.penup()
        apple.shapesize(stretch_len=0.5, stretch_wid=0.5)
        apple.color("white")
        apple.goto(self.cords) #send the apple to the generated cords
        self.apples.append(apple)

    def hide_apple(self):
        self.apples[0].ht()







