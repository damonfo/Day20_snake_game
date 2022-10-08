from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 23, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.high_score())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def high_score(self):
        with open("data.txt") as file:
            content = file.read()
            return content

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score} ", align=ALIGNMENT, font=FONT)

    def score_add(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()
