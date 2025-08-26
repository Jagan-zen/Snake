from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def collision_wall(self):
        self.write("Game over! 🐍",align="center",font = ("Arial",13,"normal"))
