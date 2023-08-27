from turtle import *
import tkinter as tk
import math

# for _ in range(3):
#     t.forward(100)  # Length of each side
#     t.left(120)     # Turn 120 degrees to form an equilateral triangle

def cono(radio, altura, t):#t es tortuga
    t.left(90)
    hipotenusa = math.hypot(radio,altura)
    angulo = math.atan(radio/altura)
    angulo = math.degrees(angulo)
    t.left(angulo)    
    print(angulo)
    t.forward(hipotenusa) 
    t.right(90-angulo)
    t.setheading(90)
    t.penup()
    t.backward(altura)
    t.left(90)
    t.forward(radio)
    t.right(90+angulo)
    t.forward(hipotenusa)
    t.pendown()
    t.backward(hipotenusa)
    t.setheading(0)
    t.right(20)
    t.circle(radio*3,40)
    if(radio >= 100):
        turtle.shape("square")


def conoTruncado(radio2,radio1,altura, t): #radio 2 es grande y radio 1 es peque
    t.penup()
    t.forward(radio2)
    t.left(90)
    t.pendown()
    positiond = t.pos()
    t.circle(radio2,180)
    positiond1 = t.pos()
    t.circle(radio2,180)
    t.penup()
    t.right(90)
    t.back(radio2)
    t.left(90)
    t.forward(altura)
    t.right(90)
    t.forward(radio1)
    t.left(90)
    t.pendown()
    t.circle(radio1,180)
    positiond2 = t.pos()
    t.circle(radio1,180)
    position2 = t.pos()
    t.goto(positiond)
    t.penup()
    t.goto(position2)
    
    t.goto(positiond1)
    t.pendown()
    t.goto(positiond2)

def hemisferio(radio, t):
    t.penup()
    t.goto(-300,-radio)
    t.pendown()
    t.circle(radio,180)
    t.penup()
    t.goto(-300,-radio)
    t.pendown()
    ovalo(radio,t)
        
def ovalo(radio,t):
    t.setheading(0)
    t.left(45)
    t.circle(radio*1.43,90)
    t.left(90)
    t.circle(radio*1.43,90)
    orPos(t)
    
def orPos(t):
    t.penup()
    t.goto(-300,0)
    
    