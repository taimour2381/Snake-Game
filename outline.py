from turtle import Turtle

class Outline(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.pencolor("white")
        for n in range(4):
            self.forward(600)
            self.left(90)
