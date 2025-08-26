import turtle as t

class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt",mode = "r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        print(self.highscore)

    def write_score(self):
        self.goto(0,280)
        self.write(f"Score:{self.score} High score:{self.highscore}",move=True,align = "center",font = ('Arial',13,"normal"))

    def score_clear(self):
        self.score += 1

    def refresh(self):
        self.clear()
        self.score_clear()
        self.write_score()

    def reset_board(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode = "w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.refresh()



    """def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER! 🐍",align="center",font = ("Arial",13,"normal"))"""