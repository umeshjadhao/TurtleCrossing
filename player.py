from turtle import Turtle

STARTING_POSITION = (0, -288)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 288


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.turtle_speed = MOVE_DISTANCE

    def go_up(self):
        self.forward(self.turtle_speed)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def level_up(self):
        self.turtle_speed +=3



