from turtle import Screen, Turtle

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")

starting_position = [(0,0),(-20,0),(-40,0)]
for position in starting_position:
    b1 = Turtle()
    b1.shape("square")
    b1.color("white")
    b1.goto(position)














screen.exitonclick()