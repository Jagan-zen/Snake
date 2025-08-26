import turtle as t
from snake import Snake
import time
from food import Food
from score_board import Score


screen = t.Screen()
screen.bgcolor("black")
screen.title("Snakes slays 🐍")
screen.setup(width = 600,height = 600)
screen.tracer(0)


score = 0
snake = Snake()
food = Food()
score_b = Score()
score_b.write_score()
screen.listen()
screen.onkey(snake.up, key = "Up")
screen.onkey(snake.down, key = "Down")
screen.onkey(snake.right, key = "Right")
screen.onkey(snake.left, key = "Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



    #for detecting the food collision
    if snake.head.distance(food) < 15:
        food.collision()
        snake.extent_seg()
        score_b.refresh()

    # for detecting collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_b.reset_board()
        snake.reset()

    # for detecting collision with tail
    if snake.collision_tail():
        food.clear_food()
        score_b.refresh()
        score_b.reset_board()
        snake.reset()

screen.exitonclick()




