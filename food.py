from turtle import Turtle
import random
from snake import Snake
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("Red")
        self.speed("fastest")
        self.collision()


    def collision(self):
        rx = random.randint(-280, 280)
        ry = random.randint(-280, 280)
        self.goto(rx, ry)

    def clear_food(self):
        self.clear()
