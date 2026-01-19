# Day 20, 21 - snake game using turtle
# learning - oop, gui control, algorithm building, array slicing

from turtle import Screen
from time import sleep
from snake import Snake
from food_and_wall import Food, Wall
from scoreboard import Scoreboard, WALL_EDGE, Instructions

# set up screen and wall
screen = Screen()
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(n=0,delay=0)
wall = Wall()
wall.draw_wall()

# Set game difficulty
title = "Game Mode"
text = "Set difficulty: Easy/Medium/Hard"
difficulty = screen.textinput(title = title, prompt = text).lower()
if difficulty == "easy": time_delay = 0.3
elif difficulty == "hard": time_delay = 0.04
else: time_delay = 0.15

# set up scoreboard, snake and food
scoreboard = Scoreboard()
snake = Snake(start_length=3)
food = Food()

def pause_game():
    screen.textinput(title = "Pause", prompt = "Press enter or click OK to resume")
    screen.listen()

# event listening
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="q", fun=scoreboard.quit_game)
screen.onkey(key="p", fun=pause_game)
screen.listen()

# Begin game
instructions = Instructions()
screen.update()
sleep(3)
instructions.clear_instructions()
game_is_on = True
screen.update()
while game_is_on:
    screen.update()
    sleep(time_delay)
    snake.move()
    # detect food
    if snake.head.distance(food.pos()) < 15:
        snake.grow()
        scoreboard.update_score()
        food.refresh()
    # detect collision with wall or voluntary quitting
    if (snake.head.xcor() > WALL_EDGE or snake.head.xcor() < -WALL_EDGE
            or snake.head.ycor() > WALL_EDGE or snake.head.ycor() < -WALL_EDGE
            or scoreboard.end_game):
        game_is_on = False
        scoreboard.game_over()
    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()