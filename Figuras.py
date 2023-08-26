import turtle
import tkinter as tk
import math

t = turtle.Turtle()

# for _ in range(3):
#     t.forward(100)  # Length of each side
#     t.left(120)     # Turn 120 degrees to form an equilateral triangle

def cono(radio2,radio1,altura): #radio 2 es grande y radio 1 es peque
    
    
    
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
 

    


    
        



  





cono(50,40,60)
input("continuar")
