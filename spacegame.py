from turtle import Screen, Turtle
import random
import time
import turtle
from tkinter import *
from tkinter import colorchooser
from threading import *
import threading
from SpacegameBullets import *
from SpacegameMeteor import *
from SpacegameInvader import *
from SpacegameTurtles import *
import turtle
energy=100
shup=False
yvar=200
score=0
wavenum=1
e=25
sib=[]
firekey="Up"
leftkey="Left"
superbullet=False
reloadingg=False
cont=0
color='white'
#c=Tk()
#c.state('zoomed')
colo = colorchooser.askcolor(title="Choose the color of your player")
print(colo)
if not colo==(None,None):
    rgb_tuple = colo[0] #gets tuple of RGB values
    color = f'#{int(rgb_tuple[0]):02x}{int(rgb_tuple[1]):02x}{int(rgb_tuple[2]):02x}'
#c.destroy()

#### Player ####
player = Turtle("arrow")
player.color(color)
player.penup()
player.tilt(90)
player.sety(-175)
player.speed('fast') 
testt=turtle.Pen()
testt.setposition(0,0)

def meteorMovement():
    if len(meteors)>0:
        for meteor in meteors:
            meteor.st()
            meteor.sety(meteor.ycor()-7)
            for bullet in bullets:
                if isCollision(bullet, meteor, 48) and bullet.Sb==False:
                    bullet.ht()
                    bullets.remove(bullet)
                elif isCollision(bullet,meteor,48) and bullet.Sb:
                    meteor.ht()
                    meteors.remove(meteor)
            if isCollision(player, meteor, 48) and shup==False:
                turtle.bye()
            if isCollision(meteor, shield, 48) and shield.isvisible():
                meteor.ht()
                meteors.remove(meteor)
                global energy
                energy-=30
                energyUpdate()
                #senergy.clear()
                #senergy.write(f"Energy:{int(energy)}", align="center",font=("Courier",24,"normal"))

            if meteor.ycor()<-230:
                meteor.ht()
                meteors.remove(meteor) 
    win.ontimer(meteorMovement,30)
def recharge():
    global energy
    if energy<100 and shup==False:
        energy+=0.20
        energyUpdate()
        #senergy.clear()
        #senergy.write(f"Energy:{int(energy)}", align="center",font=("Courier",24,"normal"))
    win.ontimer(recharge,100)
def shieldDrain():
    global energy	
    if shup==True:
        energy-=1
        energyUpdate()
        #senergy.clear()
        #senergy.write(f"Energy:{int(energy)}", align="center",font=("Courier",24,"normal"))
    win.ontimer(shieldDrain,250)
def sheildd():
    global shup
    shield.ht()
    shup=False
def sheils():
    if energy>30:   
        shield.st()
        dur.st()
        global shup
        shup=True
def sheildup():
    if energy<30:
        shield.ht()
    shield.speed('fastest')
    shield.goto(player.xcor(),player.ycor()+5)
    dur.speed('fastest')
    dur.goto(player.xcor(),player.ycor()+5)
    win.ontimer(sheildup,50)
def sis():
    for invader in enemies:
        if invader.si==True:
            sib.append(Sibullet(invader.xcor(),invader.ycor()))
    win.ontimer(sis,7000)
def clearWave():
    wave.clear()
def mm():
    danger.ht()
    dange.ht()
    meteors.append(Meteor(meteorready, 225))
def warnMeteor():
    global meteorready
    meteorready=player.xcor()
    danger.goto(meteorready, 225) 
    danger.color('red')
    danger.st()
    dange.goto(meteorready,225)
    dange.color('yellow')
    dange.st()
    win.ontimer(mm,1000)
    win.ontimer(warnMeteor,5000)
def nextwave():
    global enemies
    global xx
    global yvar
    global xxr
    global cont
    global wavenum
    for invader in enemies:
        invader.hideturtle()
        enemies.remove(invader)
    for invader in enemies:
        invader.hideturtle()
        enemies.remove(invader)
    for invader in enemies:
        invader.hideturtle()
        enemies.remove(invader)
    for invader in enemies:
        invader.hideturtle()
        enemies.remove(invader)
    wavenum+=1
    yvar=200
    xx=-175
    cont=0
    global energy
    energy=100
    energyUpdate()
    #senergy.clear()
    #senergy.write(f"Energy:{int(energy)}", align="center",font=("Courier",24,"normal"))
    wave.clear()
    wave.write(f"Wave {wavenum}!", align="center", font=("ArcadeClassic",25,"normal"))
    waves.clear()
    waves.write(f"Wave:{wavenum}", align="center", font=("Courier",24,"normal"))
    #wave.write("You get +1 max ammo",align="center", font=("ArcadeClassic",21,"normal"))
    for meteor in meteors:
        meteor.hideturtle()
        meteors.remove(meteor)
    if wavenum==2:
        xx = -175
        for invader_count in range(100):
            enemies.append(Invader(xx, yvar))
            xxr=random.randint(25,75)
            xx += xxr
            cont+=1
            if xx>=215:
                break
        xx=-175
        enemies.append(SInvader(0,yvar-50))
        cont+=1
        warnMeteor()
        #wave.clear()
    if wavenum==3:
        for invader_count in range(100):
            enemies.append(Shootinvader(xx, yvar))
            xxr=random.randint(25,75)
            xx += xxr
            cont+=1
            if xx>=215:
                break
        sis()
    if wavenum==4:
        xx = -175
        for invader_count in range(18):
            enemies.append(SInvader(xx, yvar))
            xxr=random.randint(25,75)
            xx += xxr
            cont+=1
            if xx>=215:
                break        
    player.goto(0,-175)
    win.ontimer(clearWave,2000)
def moveinvader(): 
    global enemyspeed
    global y
    for invader in enemies:
        y = invader.ycor() - 1
        invader.sety(y)
        if y<-180:
            turtle.resetscreen()
            turtle.bye()
    win.ontimer(moveinvader,70)
def stuper():
    global superbullet
    global energy
    if superbullet==False and energy>=40:
        superbullet=True 
def Super_movement():
  Superr.forward(5)
  if Superr.ycor()>195:
      Superr.ht()

def move_right():
    global energy
    if player.xcor() + playerspeed < 210:
        player.forward(playerspeed)
        energy-=0.05
        energyUpdate()
        #senergy.clear()
        #senergy.write(f"Energy:{int(energy)}", align="center", font=("Courier", 24, "normal"))
def move_left():
    global energy
    if player.xcor() - playerspeed > -210:
        player.backward(playerspeed)
        energy-=0.05
        energyUpdate()
        #senergy.clear()
        #senergy.write(f"Energy:{int(energy)}", align="center", font=("Courier", 24, "normal"))
def bullet_movement():
    for bullet in bullets:
        if bullet.isvisible and bullet.Sb:
            bullet.forward(5)
        elif bullet.isvisible():
            bullet.forward(2)
        if bullet.ycor()> 195:
            bullet.ht()
            bullets.remove(bullet)
    for bullet in sib:
        if bullet.isvisible():
            #c=bullet.ycor()-10
            bullet.sety(bullet.ycor()-2)
        if bullet.isvisible() and isCollision(bullet, shield) and shield.isvisible():
            bullet.hideturtle()
            global energy
            energy-=10
            #senergy.clear()
            #senergy.write(f"Energy:{int(energy)}", align="center", font=("Courier", 24, "normal"))
            sib.remove(bullet)
        if bullet.isvisible() and isCollision(bullet, player):
            turtle.bye()
        if bullet.ycor()<=-200:
            bullet.ht()
            sib.remove(bullet)
    win.ontimer(bullet_movement,10)
#def supermov():
   # Superr.forward(20)
    #if Superr.ycor()>195:
       # Superr.ht()
def fire_bullet():
    global superbullet
    global shup
    global energy
    if shup==False:
        if superbullet==True and energy>40:
            x,y= player.position()
            bullets.append(SBullet(x,y+20))
            for b in bullets:
                b.st()
            energy-=18
            energyUpdate()
            #senergy.clear()
            #energy.write(f"Energy:{int(energy)}", align="center",font=("Courier",24,"normal"))

            superbullet=False
        elif energy>=6:
            x,y = player.position()
            bullets.append(Bullet(x,y+20))
            for bull in bullets:
                bull.st()
            energy-=5
            energyUpdate()
            #senergy.clear()
            #senergy.write(f"Energy:{int(energy)}", align="center",font=("Courier",24,"normal"))

def isCollision(t1, t2, distance=20):
    return t1.distance(t2) < distance
def endgame():
    turtle.bye()

def energyUpdate():
    '''
    if energy*4.5-225<bar.xcor():
        bar.color('black')
        bar.goto(energy*4.5-225,-256)
        bar.color('red')
    elif energy*4.5-225>bar.xcor():
        bar.color('red')
        bar.goto(energy*4.5-225,-256)
    '''
    
    bar.up()
    bar.goto(-225,-256)
    bar.down()
    bar.clear()
    bar.goto(energy*4.5-225,-256)
def checkcollisions():
    global enemyspeed
    global y
    global cont
    global score
    global energy
    #bullet_movement()
    for invader in enemies:
        if isCollision(invader, shield,30) and shield.isvisible():
            global score
            global cont
            invader.ht()
            enemies.remove(invader)
            cont-=1
            score += 20
            energy-=10
            #senergy.clear()
            #senergy.write(f"Energy:{int(energy)}", align="center",font=("Courier",24,"normal"))

            scoreboard.clear() # Write the score
            scoreboard.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            if cont==0:
                win.ontimer(nextwave,200)
        for bullet in bullets:
            if (bullet.isvisible() and isCollision(bullet, invader)):
                    if not invader.hp==-900:
                        invader.hp -= 1
                        if bullet.Sb==True:
                            invader.hp-=1
                        if invader.hp == 1:
                            invader.color("yellow")
                        elif invader.hp <= 0 and invader.hp!=-900:
                            invader.ht()
                            enemies.remove(invader)
                            cont-=1
                            score += 20
                            energy += 6
                            if energy>100:
                                energy=100
                            energyUpdate()
                            #senergy.clear()
                            #senergy.write(f"Energy:{int(energy)}", align="center",font=("Courier",24,"normal"))
                            scoreboard.clear() # Write the score
                            scoreboard.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
                            if cont==0:
                                win.ontimer(nextwave,200)
                        bullet.ht()
                        bullets.remove(bullet)
                    elif invader.hp==-900:   
                        if bullet.Sb==False:
                            invader.ht()
                            cont+=1
                            for i in range(2):
                                global e
                                enemies.append(Invader(invader.xcor()-e,invader.ycor()))
                                e*=-1
                        elif bullet.Sb==True:
                            invader.ht()
                            enemies.append(Invader(invader.xcor(),invader.ycor()))
                        bullet.ht()
                        bullets.remove(bullet)
                        enemies.remove(invader)                        
    win.update()
    win.ontimer(checkcollisions, 40)
#### Window ####

win = turtle.Screen()
win.bgcolor("black")
win.title('Space Invaders')
win.tracer(False)

border_pen = Turtle(visible=False)
border_pen.speed('fastest')
border_pen.color("white")
border_pen.pensize(3)

border_pen.penup()
border_pen.setposition(-225, -225)
border_pen.pendown()

for _ in range(4):
    border_pen.forward(450)
    border_pen.left(90)

sheildup()
score = 0
### Bullets ###
global bullets
global enemies
bullets=[]
enemies = []
meteors=[]
xx = -175
for invader_count in range(100):
        enemies.append(Invader(xx, yvar))
        xxr=random.randint(25,75)
        xx += xxr
        cont+=1
        if xx>=215:
            break
playerspeed = 10
enemyspeed = 1.4
win.onkeypress( move_left, 'Left')
win.onkeypress( move_right, 'Right')
win.onkeypress(sheils, 'e')
win.onkey(sheildd, 'e')
win.onkeypress(sheils, 'E')
win.onkey(sheildd, 'E')
win.onkey(fire_bullet, firekey)
win.onkey(stuper,'s')
win.onkey(stuper, 'S')
win.onkey(endgame,'Escape')
win.onkey(nextwave,'p')
win.listen()
moveinvader()
win.setup(width=1.0, height=1.0)
canvas = win.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
checkcollisions()
bullet_movement()
meteorMovement()
recharge()
drawbar()
shieldDrain()
win.mainloop()
turtle.mainloop()