
from snake import Culebrita
from turtle import Screen, distance
from puntos import Puntos
from score import Score
import time

snake = Culebrita()
puntos = Puntos()
score = Score()
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
    #! Crecimiento  de la culebrita y aumento del marcador
    if snake.head.distance(puntos) < 15:
        puntos.new_location
        score.score_points
        snake.grow_snake
    #! Limite del tablero de juego
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.game_over
        band = False
    #! Finalizando el juego si toca su cola la culebrita
    for i in snake.segments:
        if i == snake.head:
            pass
        elif snake.head.distance(i) < 10:
            score.game_over
            band = False

screen.exitonclick()