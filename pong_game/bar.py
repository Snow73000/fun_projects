from turtle import Turtle
from wall import WALL_HEIGHT

BAR_PACE = 30 # default value, changes with difficulty level
BAR_SHAPE = "square"
BAR_COLOR = "white"
BAR_HEIGHT = 100
BAR_WIDTH = 20
UP = 90

class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pace = BAR_PACE
        self.shape(BAR_SHAPE)
        self.color(BAR_COLOR)
        self.setheading(UP)
        self.shapesize(stretch_wid=BAR_WIDTH/20, stretch_len=BAR_HEIGHT / 20)

    def move_up(self):
        if self.ycor() < WALL_HEIGHT - (BAR_HEIGHT / 2):
            self.forward(self.pace)

    def move_down(self):
        if self.ycor() > -WALL_HEIGHT + (BAR_HEIGHT / 2):
            self.backward(self.pace)