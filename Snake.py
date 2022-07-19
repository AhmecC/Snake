from turtle import Turtle

class Snake():
    def __init__(self): #Initialises the Snake class, when the object is first created this is what is given too it
        self.snake_body = [] #This is a list containing the snakes body
        self.create_snake() #This calls the function that creates the snakes body (called when an object is made)
        self.head = self.snake_body[0] #defines the head of the snake for simplicity

    def create_snake(self):
        X = [0, -20, -40] #generate 3 squares, on behind the other
        for i in range(0,3):
            bola = Turtle(shape="square")  # as a square, penup so no line and its white
            bola.penup()
            bola.speed(0)
            bola.shapesize(stretch_wid=0.5)
            bola.color("dark green")
            bola.goto(X[i], 0)  # sets what position it goes to
            self.snake_body.append(bola) #the list for attributes of the obejct is reffered to here


    def reset(self):
        for entry in self.snake_body:
            entry.goto(500,500)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]


    def extra_body(self):
        last = self.snake_body[-1].pos()
        bola = Turtle(shape = "square")
        bola.penup()
        bola.speed(0)
        bola.shapesize(stretch_wid=0.5)
        bola.color("dark green")
        if self.snake_body[-1].heading() == 90 or 270:
            bola.goto(last[0], last[1]-20)
        else:
            bola.goto(last[0]-20, last[1])
        self.snake_body.append(bola)

    def move(self):
        for seg_num in range(len(self.snake_body) -1, 0, -1): #goes from 2 to 0 # (steps of -1)
            new_x = self.snake_body[seg_num -1].xcor() #finds the x and y coordinate of the next square
            new_y = self.snake_body[seg_num -1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y) #tells the initial (last) square to move where the next square was
        self.head.forward(20) #tells the first entry to go forward by 20

    def up(self):
        if self.head.heading() != 270: #set heading is the set angles that the module uses, so 90 is always upward
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def outside_border(self): #checks if they are inside the border or not
        if self.head.ycor() >= 300 or self.head.ycor() <= -300:
            return False
        if self.head.xcor() >= 300 or self.head.xcor() <= -300:
            return False

