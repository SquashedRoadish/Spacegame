import turtle
from turtle import Turtle
class Invader(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__(shape="turtle")
        self.color("red")
        self.penup()
        self.setposition(xcor, ycor)
        self.tilt(-90)
        self.speed('slow')
        self.hp = 2
        self.si=False
class Shootinvader(Turtle):
    def __init__(self,xs,ys):
        super().__init__(shape='turtle')
        self.color('green')
        self.hp= 2
        self.speed('fastest')
        self.si=True
        self.penup()
        self.setposition(xs,ys)
        self.tilt(-90)
        self.speed('slow')
class SInvader(Turtle):
    def __init__(self,xcort,ycort):
        super().__init__(shape="turtle")
        self.color("Blue")
        self.speed('fastest')
        self.penup()
        self.setposition(xcort,ycort)
        self.tilt(-90)
        self.speed('slow')
        self.hp= -900
        self.si=False