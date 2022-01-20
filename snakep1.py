from snake import Culebrita
from turtle import Screen
from puntos import Puntos
import time

snake = Culebrita()
puntos = Puntos()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("El juego de la culebrita")
screen.tracer(0) 
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")


band = True
while band:
    screen.update()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()