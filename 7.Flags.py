import turtle
import random

bob = turtle.Turtle()

points = 0
lives = 3

def Italy():
    bob.pu()
    bob.goto(-60, 60)
    bob.pd()
    bob.color("green", "green")
    bob.begin_fill()
    for i in range(2):
        bob.fd(90)
        bob.rt(90)
        bob.fd(180)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(-60, 60)
    bob.fd(180)
    bob.pd()
    bob.color("red", "red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(90)
        bob.rt(90)
        bob.fd(180)
        bob.rt(90)
    bob.end_fill()

def France():
    bob.pu()
    bob.goto(-60, 60)
    bob.pd()
    bob.color("blue", "blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(90)
        bob.rt(90)
        bob.fd(180)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(-60, 60)
    bob.fd(180)
    bob.pd()
    bob.color("red", "red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(90)
        bob.rt(90)
        bob.fd(180)
        bob.rt(90)
    bob.end_fill()

def Germany():
    bob.pu()
    bob.goto(-60, 60)
    bob.pd()
    bob.color("black", "black")
    bob.begin_fill()
    for i in range(2):
        bob.fd(270)
        bob.rt(90)
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(-60, 15)
    bob.pd()
    bob.color("red", "red")
    bob.begin_fill()
    for i2 in range(2):
        bob.fd(270)
        bob.rt(90)
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(-60, -30)
    bob.pd()
    bob.color("yellow", "yellow")
    bob.begin_fill()
    for i3 in range(2):
        bob.fd(270)
        bob.rt(90)
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()

def Finland():
    bob.pu()
    bob.goto(60, -60)
    bob.pencolor("black")
    bob.pd()
    for d in range(2):
        bob.fd(350)
        bob.rt(90)
        bob.fd(250)
        bob.rt(90)
    bob.pu()
    bob.fd(90)
    bob.color("blue", "blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(45)
        bob.rt(90)
        bob.fd(250)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(60, -60)
    bob.rt(90)
    bob.fd(83)
    bob.lt(90)
    bob.begin_fill()
    for i2 in range(2):
        bob.fd(350)
        bob.rt(90)
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()

def Poland():
    bob.pu()
    bob.goto(60, -60)
    bob.pd()
    bob.pencolor("black")
    for d in range(2):
        bob.fd(350)
        bob.rt(90)
        bob.fd(250)
        bob.rt(90)
    bob.pu()
    bob.goto (60, -60)
    bob.rt(90)
    bob.fd(125)
    bob.lt(90)
    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(350)
        bob.rt(90)
        bob.fd(125)
        bob.rt(90)
    bob.end_fill()

def Greece():
    bob.pu()
    bob.goto(60, -60)
    bob.pd()
    bob.pencolor("black")
    for d in range(2):
        bob.fd(350)
        bob.rt(90)
        bob.fd(200)
        bob.rt(90)

    bob.color("DodgerBlue", "DodgerBlue")
    bob.begin_fill()
    for i in range(4):
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(130, -60)
    bob.pd()
    bob.begin_fill()
    for i2 in range(4):
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.rt(90)
    bob.fd(70)
    bob.lt(90)
    bob.pd()
    bob.begin_fill()
    for i3 in range(4):
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.bk(70)
    bob.pd()
    bob.begin_fill()
    for i4 in range(4):
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(60, -60)
    bob.fd(115)
    bob.begin_fill()
    for i5 in range(2):
        bob.fd(235)
        bob.rt(90)
        bob.fd(23)
        bob.rt(90)
    bob.end_fill()

    bob.rt(90)
    bob.fd(46)
    bob.lt(90)

    bob.begin_fill()
    for i6 in range(2):
        bob.fd(235)
        bob.rt(90)
        bob.fd(23)
        bob.rt(90)
    bob.end_fill()

    bob.rt(90)
    bob.fd(46)
    bob.lt(90)

    bob.begin_fill()
    for i7 in range(2):
        bob.fd(235)
        bob.rt(90)
        bob.fd(23)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(60, -60)
    bob.rt(90)
    bob.fd(138)
    bob.lt(90)
    bob.pd()

    bob.begin_fill()
    for i8 in range(2):
        bob.fd(350)
        bob.rt(90)
        bob.fd(23)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(60, -60)
    bob.rt(90)
    bob.fd(184)
    bob.lt(90)
    bob.pd()

    bob.begin_fill()
    for i8 in range(2):
        bob.fd(350)
        bob.rt(90)
        bob.fd(23)
        bob.rt(90)
    bob.end_fill()

def UAE():
    bob.pu()
    bob.goto(-60, 60)
    bob.pd()
    bob.color("green", "green")
    bob.begin_fill()
    for i in range(2):
        bob.fd(270)
        bob.rt(90)
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(-60, 15)
    bob.pd()
    bob.color("black", "white")
    bob.begin_fill()
    for i2 in range(2):
        bob.fd(270)
        bob.rt(90)
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(-60, -30)
    bob.pd()
    bob.color("black", "black")
    bob.begin_fill()
    for i3 in range(2):
        bob.fd(270)
        bob.rt(90)
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(-60, 60)
    bob.pd()
    bob.color("red", "red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(67.5)
        bob.rt(90)
        bob.fd(135)
        bob.rt(90)
    bob.end_fill()

def Palestine():
    bob.pu()
    bob.goto(-60, 60)
    bob.pd()
    bob.color("black", "black")
    bob.begin_fill()
    for i in range(2):
        bob.fd(270)
        bob.rt(90)
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(-60, 15)
    bob.pd()
    bob.color("black", "white")
    bob.begin_fill()
    for i2 in range(2):
        bob.fd(270)
        bob.rt(90)
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(-60, -30)
    bob.pd()
    bob.color("green", "green")
    bob.begin_fill()
    for i3 in range(2):
        bob.fd(270)
        bob.rt(90)
        bob.fd(45)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(-60, 60)
    bob.pd()
    bob.color("red", "red")
    bob.begin_fill()
    bob.rt(90)
    for i4 in range(3):
        bob.fd(135)
        bob.lt(120)
    bob.end_fill()

#list of flags
flags = [Italy, France, Germany, Finland, Poland, Greece, UAE, Palestine]

while lives>0 and len(flags)>0:
    bob.reset()
    bob.speed(200)
    flag=random.choice(flags)
    flag()
    answer=input("Flag name: ")

    if answer == flag.__name__:
        print("gg")
        points = points +10
        print("Points:", points)
        print("Lives:", lives)
        flags.remove(flag)
    else:
        print("lol -1")
        if points>0:
            points = points -10
        else:
            points =0
        lives = lives -1
        print("Points:", points)
        print("Lives:", lives)
        flags.remove(flag)

print("gg wp")
#Italy()
#France()
#Germany()
#Finland()
#Poland()
#Greece()
#UAE()
#Palestine()