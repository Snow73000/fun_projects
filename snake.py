from turtle import Turtle

SNAKE_COLOR = "white"
HEAD_COLOR = "azure4"
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self, start_length=3):
        self.segments = []
        self.segment_size = 0
        self.start_length = start_length
        self.create_snake()
        self.head = self.segments[0]
        self.snake_has_moved = False

    def create_snake(self):
        for i in range(self.start_length):
            new_segment = Turtle(shape='square')
            new_segment.color(SNAKE_COLOR)
            new_segment.penup()
            self.segments.append(new_segment)
        self.segments[0].color(HEAD_COLOR)
        self.segment_size = self.segments[0].get_shapepoly()[1][1] - self.segments[0].get_shapepoly()[0][1]
        starting_positions = []
        for i, segment in enumerate(self.segments):
            segment.setposition(-self.segment_size*i,0)
            starting_positions.append(segment.pos())

    def move(self):
        self.snake_has_moved = True
        for seg_num in range(len(self.segments) - 1, -1, -1):
            if seg_num == 0:
                self.head.forward(self.segment_size)
                continue
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())


    def right(self):
        if self.head.heading() != LEFT and self.snake_has_moved:
            self.head.setheading(RIGHT)
            self.snake_has_moved = False

    def left(self):
        if self.head.heading() != RIGHT and self.snake_has_moved:
            self.head.setheading(LEFT)
            self.snake_has_moved = False

    def up(self):
        if self.head.heading() != DOWN and self.snake_has_moved:
            self.head.setheading(UP)
            self.snake_has_moved = False

    def down(self):
        if self.head.heading() != UP and self.snake_has_moved:
            self.head.setheading(DOWN)
            self.snake_has_moved = False

    def grow(self):
        new_segment = Turtle(shape='square')
        new_segment.setposition(self.segments[-1].pos())
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        self.segments.append(new_segment)

