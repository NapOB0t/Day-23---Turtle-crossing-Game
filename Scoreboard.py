from turtle import Turtle

level_increment = 1
LEVEL = 1

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-260, y=260)
        self.write(f"Level : {LEVEL}", font="calibre")
        self.hideturtle()

    def levelUpdate(self):
        self.clear()
        level_up = LEVEL + level_increment
        self.penup()
        self.goto(x=-260, y=260)
        self.write(f"Level : {level_up}", font="calibre")




    def gameover(self):

        game_over = Turtle()
        game_over.write(arg=f"Game over ", font="Calibre")
        game_over.color("white")





