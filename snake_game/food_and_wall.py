from turtle import Turtle
from random import randint
from scoreboard import WALL_EDGE

FOOD_SIZE = 0.5
FOOD_SHAPE = "circle"
FOOD_COLOR = "green"
FOOD_RANGE = (-WALL_EDGE+10, WALL_EDGE-10)
WALL_COLOR = "red"
MOVE_SPEED = "fastest"

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.shapesize(stretch_wid=FOOD_SIZE, stretch_len=FOOD_SIZE)
        self.penup()
        self.color(FOOD_COLOR)
        self.speed(MOVE_SPEED)
        self.refresh()

    def refresh(self):
        self.goto(x=randint(*FOOD_RANGE), y=randint(*FOOD_RANGE))

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.color(WALL_COLOR)
        self.speed(MOVE_SPEED)
        self.hideturtle()
        self.penup()

    def draw_wall(self):
        self.setposition(WALL_EDGE, WALL_EDGE)
        self.pendown()
        self.goto(WALL_EDGE, -WALL_EDGE)
        self.goto(-WALL_EDGE, -WALL_EDGE)
        self.goto(-WALL_EDGE, WALL_EDGE)
        self.goto(WALL_EDGE, WALL_EDGE)
