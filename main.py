import time
from turtle import Screen
from Apple import Apple
from Snake import Snake
from Scoreboard import Scoreboard
from Messages import Message

#High Score is 46


truth = False
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.listen()
screen.tracer(0)

snake = Snake()
score = Scoreboard()
screen.update()
time.sleep(1)

count = 0
game_on = True
while game_on:
    count +=1
    screen.update()
    time.sleep(0.1)
    snake.move()
    if count == 1:
        apple = Apple()
        cords = apple.cords
    if snake.head.distance(cords) < 15:
        snake.extra_body()
        score.increase_score()
        count = 0
        apple.hide_apple()
    for entry in snake.snake_body[1:]:
        location = entry.position()
        if snake.head.distance(location) < 15:
            # game_on = False
            score.reset()
            snake.reset()
            time.sleep(1)

    screen.onkey(key="w", fun=snake.up)
    screen.onkey(key="a", fun=snake.left)
    screen.onkey(key="s", fun=snake.down)
    screen.onkey(key="d", fun=snake.right)
    screen.onkey(key="W", fun=snake.up)
    screen.onkey(key="A", fun=snake.left)
    screen.onkey(key="S", fun=snake.down)
    screen.onkey(key="D", fun=snake.right)
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Right", fun=snake.right)
    scores = score.eaten
    if snake.outside_border() == False:
        # game_on = False
        score.reset()
        snake.reset()
        time.sleep(1)


#  message = Message()
# message.end()


screen.exitonclick()