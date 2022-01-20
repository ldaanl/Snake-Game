from turtle import Turtle
from random import randint

class Puntos(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('circle')
        self.color('purple')
        self.shapesize(0.5,0.5)
        self.speed('fastest')
        self.new_location
    
    @property
    def new_location(self):
        x = randint(-280, 280)
        y = randint(-280,280)
        self.goto(x,y)
