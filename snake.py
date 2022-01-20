from turtle import Turtle

coo_seg = [(0, 0), (-20, 0), (-40, 0)] #* Coordenadas iniciales

class Culebrita:
    def __init__(self):
        self.segments = []
        self.snake_init()
        self.head = self.segments[0]
    
    def snake_init(self):
        #* Creación del cuerpo principal
        for i in coo_seg:
            self.append_block(i)
    
    def append_block(self,i):
        segment = Turtle("square")
        segment.color("white")
        segment.pu()
        segment.goto(i)
        self.segments.append(segment)
    
    @property
    def grow_snake(self):
        self.append_block(self.segments[-1].position())
    
    def move(self):
        #* Movimiento unificado de los tres segmentos
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


