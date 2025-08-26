import turtle as t
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
MOVE_DIST = 15
snake_start = [(-20,0),(0,0),(20,0)]
class Snake():
    def __init__(self):
        self.snakes_list = []
        self.create_snake()
        self.head = self.snakes_list[0]

    def create_snake(self):
        for i in snake_start:
            self.add_segment(i)

    def add_segment(self,position):
        new_seg = t.Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.snakes_list.append(new_seg)

    def extent_seg(self):
        self.add_segment(self.snakes_list[-1].pos())

    def collision_tail(self):
        for i in self.snakes_list[3:]:
            if self.head.distance(i) < 10:
                return True
        return False

    def reset(self):
        for seg in self.snakes_list:
            seg.goto(1000,1000)
        self.snakes_list.clear()
        self.create_snake()
        self.head = self.snakes_list[0]

    def move(self):
        for i in range(len(self.snakes_list) - 1, 0, -1):
            nx = self.snakes_list[i - 1].xcor()
            ny = self.snakes_list[i - 1].ycor()
            self.snakes_list[i].goto(nx, ny)
        self.snakes_list[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)





