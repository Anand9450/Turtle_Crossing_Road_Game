from turtle import Turtle
START_LOC = (0,-250)
MOV_DISTANCE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOV_DISTANCE)

    def go_to_start(self):
        self.goto(START_LOC)
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
