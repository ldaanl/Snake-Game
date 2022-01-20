from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.write('SCORE: {}'.format(self.score), align = 'center')
        

