from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
  def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.setposition(-230, 270)
        self.update_scoreboard()


  def update_scoreboard(self):
        self.write(f"Level = {self.score} ", False, align="center",font= FONT)


  def scoreincrease(self):
        self.score += 1
        self.clear()
        self.write(f"Level = {self.score} ", False, align="center",font= FONT)


  def gameover(self):
        self.goto(0, 0)
        self.write("Game Over ", False, align="center",font= FONT)
