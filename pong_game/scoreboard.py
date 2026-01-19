from turtle import Turtle
from wall import WALL_WIDTH, WALL_HEIGHT

TEXT_ALIGNMENT = "center"
TEXT_FONT = ("Courier", int(WALL_WIDTH/24), "normal")
SCORE_FONT = ("Courier", int(WALL_WIDTH/12), "normal")
TEXT_COLOR = "white"
LEFT_SCORE_POSITION = (-40, WALL_HEIGHT - 50)
RIGHT_SCORE_POSITION = (40, WALL_HEIGHT - 50)
INSTRUCTIONS = ("Press arrow keys (^ v) to move right board up/down\nPress w/s to move "
                "left board up/down\nPress p to pause game\nPress q to quit during game")
INSTRUCT_POS = (0,0)
GAME_OVER_POS = (0,0)
GAME_OVER_TEXT = "GAME OVER\nClick screen to exit"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_player_score = 0
        self.right_player_score = 0
        self.end_game = False
        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setposition(LEFT_SCORE_POSITION)
        self.write(arg=f"{self.left_player_score}", align=TEXT_ALIGNMENT, font=SCORE_FONT)
        self.setposition(RIGHT_SCORE_POSITION)
        self.write(arg=f"{self.right_player_score}", align=TEXT_ALIGNMENT, font=SCORE_FONT)

    def update_left_score(self):
        self.left_player_score += 1
        self.update_scoreboard()

    def update_right_score(self):
        self.right_player_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setposition(GAME_OVER_POS)
        self.write(arg=GAME_OVER_TEXT, align=TEXT_ALIGNMENT, font=TEXT_FONT)

    def quit_game(self):
        self.game_over()
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