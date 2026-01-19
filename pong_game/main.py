# pong game using turtle
# see: https://docs.python.org/3/library/turtle.html
# see also: https://github.com/python/cpython/blob/3.14/Lib/turtle.py

from turtle import Screen
from wall import Wall, WALL_WIDTH, WALL_HEIGHT
from bar import Bar, BAR_WIDTH, BAR_HEIGHT
from scoreboard import Scoreboard, Instructions
from ball import Ball, BALL_WIDTH, BALL_PACE
from time import sleep

# set up screen and wall
screen = Screen()
screen.title('Pong Game')
screen.setup(width=(WALL_WIDTH+10)*2, height=(WALL_HEIGHT+10)*2)
screen.bgcolor("black")
screen.tracer(n=0,delay=0)
wall = Wall()
wall.draw_wall()
wall.draw_mid_line()

# set up scoreboard and bars
scoreboard = Scoreboard()
bar_right = Bar()
bar_left = Bar()
bar_right.setposition(WALL_WIDTH - BAR_WIDTH/2,0)
bar_left.setposition(-WALL_WIDTH + BAR_WIDTH/2,0)

# Set game difficulty
title = "Game Mode"
text = "Set difficulty: Easy/Medium/Hard"
difficulty = screen.textinput(title = title, prompt = text).lower()
if difficulty == "medium":
    move_speed = 0.005
    bar_left.pace = 40
    bar_right.pace = 40
elif difficulty == "hard":
    move_speed = 0.003
    bar_left.pace = 50
    bar_right.pace = 50
else:
    move_speed = 0.01
    bar_left.pace = 20
    bar_right.pace = 20

# game pause and event listening
def pause_game():
    screen.textinput(title = "Pause", prompt = "Press enter or click OK to resume")
    screen.listen()

screen.onkeypress(key="Up", fun=bar_right.move_up)
screen.onkeypress(key="Down", fun=bar_right.move_down)
screen.onkeypress(key="w", fun=bar_left.move_up)
screen.onkeypress(key="s", fun=bar_left.move_down)
screen.onkey(key="q", fun=scoreboard.quit_game)
screen.onkey(key="p", fun=pause_game)
screen.listen()

# show instructions and ball
instructions = Instructions()
screen.update()
sleep(2.5)
instructions.clear_instructions()
ball = Ball(move_speed=move_speed)
bar_ball_gap = BAR_WIDTH/2 + BALL_WIDTH/2 + BALL_PACE/2
sleep(1)

# Begin game
game_is_on = True
while game_is_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()
    is_ball_at_left_edge = (ball.xcor() < bar_left.xcor() + bar_ball_gap)
    is_ball_at_right_edge = (ball.xcor() > bar_right.xcor() - bar_ball_gap)
    is_ball_at_left_bar = ((ball.ycor() < bar_left.ycor() + BAR_HEIGHT / 2)
                           and (ball.ycor() > bar_left.ycor() - BAR_HEIGHT / 2))
    is_ball_at_right_bar = ((ball.ycor() < bar_right.ycor() + BAR_HEIGHT / 2)
                            and (ball.ycor() > bar_right.ycor() - BAR_HEIGHT / 2))
    # detect collision with wall
    if ((ball.ycor() < -WALL_HEIGHT + BALL_WIDTH / 2)
            or (ball.ycor() > WALL_HEIGHT - BALL_WIDTH / 2)):
        ball.wall_bounce()
    # detect collision with bar
    elif ((is_ball_at_left_edge and is_ball_at_left_bar)
          or (is_ball_at_right_edge and is_ball_at_right_bar)):
        ball.bar_bounce()
    # ball exceeds right; left scores
    elif is_ball_at_right_edge and not is_ball_at_right_bar:
        while ball.xcor() < WALL_WIDTH + BALL_WIDTH/2:
            screen.update()
            sleep(ball.move_speed)
            ball.move()
        scoreboard.update_left_score()
        ball.reset_ball(move_speed=move_speed)
        sleep(1)
    # ball exceeds left; right scores
    elif is_ball_at_left_edge and not is_ball_at_left_bar:
        while ball.xcor() > -WALL_WIDTH - BALL_WIDTH/2:
            screen.update()
            sleep(ball.move_speed)
            ball.move()
        scoreboard.update_right_score()
        ball.reset_ball(move_speed=move_speed)
        sleep(1)
    # game is voluntarily ended
    if scoreboard.end_game:
        game_is_on = False


screen.exitonclick()
