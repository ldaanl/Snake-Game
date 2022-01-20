from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0,260)
        self.hideturtle()
        self.score_text
    
    @property
    def score_text(self):
        self.write('SCORE: {}'.format(self.score), align = 'center', font = ('Arial', 25, 'normal'))
    
    @property
    def score_points(self):
        self.score += 1
        self.clear()
        self.score_text
    
    @property
    def game_over(self):
        self.pu()
        self.goto(0,0)
        self.color('blue')
        self.write('GAME OVER', align = 'center', font = ('Arial', 25, 'normal'))




