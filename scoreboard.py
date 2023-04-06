from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="left",font=("arial",8,"normal"))


    def scored(self):
        self.score+= 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}" , align="left", font=("arial", 8, "normal"))

    def reset(self):
        if self.score >= self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()



        #self.goto(0,0)
        #self.write(f"GAME OVER", align="center", font=("arial",20,"normal"))

