from turtle import Turtle
import turtle
meteors=[]
class Meteor(Turtle):
    def __init__(self,xxx,yyy):
        super().__init__(shape='circle')
        self.color('brown')
        self.penup()
        self.speed('fastest')
        self.goto(xxx,yyy)
        self.speed('slowest')
        self.shapesize(3.5,3.5)
        self.ht()