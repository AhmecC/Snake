from turtle import Turtle


#it inherits from the turtle class to give it functionality to change numbers
#write() scoreboard

class Scoreboard(Turtle):
    def __init__(self):
        super(). __init__()
        self.ht()
        self.eaten = 0
        with open("Scorekeeper.txt", mode="r") as file:
            da_score = file.read()
        self.high_score = int(da_score)
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update()

    def update(self):
        self.goto(0, 270)
        self.write(f"Score: {self.eaten}  High Score: {self.high_score}", True, align="center", font=("Calibri", 20, "normal"))

    def increase_score(self):
        self.eaten +=1
        self.clear()
        self.update()

    def reset(self):
        if self.eaten > self.high_score:
            self.high_score = self.eaten
            with open("Scorekeeper.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.eaten = 0
        self.clear()
        self.update()

#collision with own tail
