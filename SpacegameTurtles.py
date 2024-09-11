import turtle
from turtle import Turtle
wavenum=1
score=0
energy=100
#WaveNumber
wave=turtle.Pen()
wave.pencolor("white")
wave.ht()
wave.down()
wave.clear()
#Scoreboard
scoreboard = turtle.Pen()
scoreboard.penup()
scoreboard.ht()
scoreboard.color('white')
scoreboard.speed("fastest")
scoreboard.goto(-150, 235)
scoreboard.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
#WaveNumberMini
waves= turtle.Pen()
waves.up()
waves.ht()
waves.setposition(150,235)
waves.color("White")
waves.write(f"Wave:{wavenum}", align="center", font=("Courier",24,"normal"))
#Energy
#senergy=turtle.Pen()
#senergy.ht()
#senergy.up()
#senergy.color("White")
#senergy.setposition(100,-259)
#senergy.write(f"Energy:{energy}", align="center", font=("Courier", 24, "normal"))
#Reload
reloading=turtle.Pen()
reloading.ht()
reloading.up()
reloading.color("White")
reloading.setposition(0,-259)
#Incoming meteor
danger=turtle.Pen()
danger.ht()
danger.shape('triangle')
danger.tilt(90)
danger.speed('fastest')
danger.up()
danger.shapesize(2.8,2.8)
dange=turtle.Pen()
dange.ht()
dange.shape('triangle')
dange.shapesize(1.4,1.4)
dange.tilt(90)
dange.speed('fastest')
dange.up()
#Sheild
shield=turtle.Pen()
shield.hideturtle()
shield.up()
shield.shape('circle')
shield.shapesize(2.75,2.75)
shield.color('blue')
dur=turtle.Pen()
dur.up()
dur.shapesize(2,2)
dur.shape('circle')
dur.color('black')
dur.ht()
#energy bar
bar=turtle.Pen()
bar.ht()
bar.up()
bar.shape('square')
bar.color('red')
bar.width(20)
bar.setposition(-225,-256)
bar.speed('fastest')
def drawbar():
    global bar
    bar.down()
    bar.forward(450)
#energy bar cover thingy