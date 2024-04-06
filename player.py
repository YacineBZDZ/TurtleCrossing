import turtle as t
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.y_move = 20

    def Up(self):
        self.forward(MOVE_DISTANCE)

    def resetPoistion(self):
        self.goto(STARTING_POSITION)
