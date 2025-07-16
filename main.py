from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food


screen = Screen()
screen.title("Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()


snake.create_snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#detecat collision with food
    if snake.head.distance(food) < 15:
        food.refresh()










screen.exitonclick()