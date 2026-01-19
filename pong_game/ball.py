from turtle import Turtle
from random import choice as rand_choice

BALL_SHAPE = "circle"
BALL_COLOR = "white"
BALL_PACE = 2
BALL_WIDTH = 20
ANGLES = (list(range(10,71)) + list(range(110,171)) +
          list(range(190,251)) + list(range(290,351)))

class Ball(Turtle):
    def __init__(self, move_speed = 0.01):
        super().__init__()
        self.penup()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.shapesize(stretch_wid=BALL_WIDTH/20, stretch_len=BALL_WIDTH/20)
        self.reset_ball()
        self.move_speed = move_speed

    def move(self):
        self.forward(BALL_PACE)

    def wall_bounce(self):
        self.setheading(360 - self.heading())

    def bar_bounce(self):
        self.setheading((180 - self.heading()) % 360)
        self.move_speed *= 0.8

    def reset_ball(self, move_speed = 0.01):
        self.goto(0,0)
        self.setheading(rand_choice(ANGLES))
        self.move_speed = move_speed