
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("El juego de la culebrita")
screen.tracer(0)

first_snake = [(0,0), (-20,0), (-40,0)]
segments = []

for i in first_snake:
    segment = Turtle("square")
    segment.color("white")
    segment.pu()
    segment.goto(i)
    segments.append(segment)

band = True
while band:
    screen.update()
    for i in segments:
        i.forward(10)
        time.sleep(0.5)


screen.exitonclick()