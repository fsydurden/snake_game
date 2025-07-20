from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier"
TEXT = "normal"
FONT_SIZE = 24
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())

        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()




    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=(FONT, FONT_SIZE, TEXT))



    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.color("white")
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=(FONT, FONT_SIZE, TEXT))



    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
