from turtle import Turtle,Screen
from SpacegameTurtles import *
class Bullet(Turtle):
    def __init__(self,xuu,yuu):
        super().__init__(shape="arrow", visible=False)
        self.shapesize(.5, 1)
        self.color("yellow")
        self.penup()
        self.setheading(90)
        self.speed('fast')
        self.goto(xuu,yuu)
        self.Sb=False

    
class SBullet(Turtle):
    def __init__(self,xii,yii):
        super().__init__(shape="arrow", visible=False)
        self.shapesize(.5,1)
        self.color("orange")
        self.penup()
        self.setheading(90)
        self.speed('fast')
        self.goto(xii,yii)
        self.Sb=True
class Sibullet(Turtle):
    def __init__(self,sx,sy):
        super().__init__(shape='arrow')
        self.setheading(180)
        self.shapesize(.5,1)
        self.tilt(90)
        self.penup()
        self.color('red')
        self.Sb=False
        self.speed('fast')
        self.goto(sx,sy)


