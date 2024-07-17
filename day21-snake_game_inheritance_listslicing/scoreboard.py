from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNEMENT, font=FONT)

    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNEMENT, font=FONT)
        

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()