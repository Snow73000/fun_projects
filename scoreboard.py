from turtle import Turtle

TEXT_ALIGNMENT = "center"
TEXT_FONT = ("Courier", 18, "normal")
TEXT_COLOR = "white"
WALL_EDGE = 270
SCORE_POSITION = (0,WALL_EDGE)
INSTRUCTIONS = "Use arrow keys to move: ^ v < >\nAvoid red walls\nAvoid colliding with self\nPress p to pause game\nPress q to quit during game"
INSTRUCT_POS = (0, 0)
GAME_OVER_POS = (0,0)
GAME_OVER_TEXT = "GAME OVER\nClick screen to exit"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.end_game = False
        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()
        self.setposition(SCORE_POSITION)
        self.write(arg=f"Score: {self.score}", align=TEXT_ALIGNMENT, font=TEXT_FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align=TEXT_ALIGNMENT, font=TEXT_FONT)

    def game_over(self):
        self.setposition(GAME_OVER_POS)
        self.write(arg=GAME_OVER_TEXT, align=TEXT_ALIGNMENT, font=TEXT_FONT)

    def quit_game(self):
        self.end_game = True

class Instructions(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(TEXT_COLOR)
        self.penup()
        self.setposition(INSTRUCT_POS)
        self.write(arg=INSTRUCTIONS, align=TEXT_ALIGNMENT, font=TEXT_FONT)

    def clear_instructions(self):
        self.clear()