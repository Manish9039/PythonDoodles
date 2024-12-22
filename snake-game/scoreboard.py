from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Times New Roman', 16, 'normal')
class Score(Turtle):

    def __init__(self):
        self.current_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setpos(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as file:
                file.write(str(self.current_score))
        self.current_score = 0
        self.update_scoreboard()

    def give_score(self):
        self.current_score += 1
        self.update_scoreboard()