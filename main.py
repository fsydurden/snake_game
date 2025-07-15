from turtle import Screen, Turtle

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")

b1 = Turtle()
b1.shape("square")
b1.color("white")
b2 = Turtle()
b2.shape("square")
b2.color("white")
b2.goto(x=-20, y=0)
b3 = Turtle()
b3.shape("square")
b3.color("white")
b3.goto(x=-40, y=0)














screen.exitonclick()