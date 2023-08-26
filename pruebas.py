import turtle
import tkinter as tk

def draw_grid(step, size):
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(i, -size)
        turtle.pendown()
        turtle.goto(i, size)
        
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(-size, i)
        turtle.pendown()
        turtle.goto(size, i)


def mainpos(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(-screensize,0)
    tortuga.pendown()

def xbar(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(-screensize,0)
    tortuga.pendown()
    tortuga.back(-screensize)
    tortuga.forward(screensize-20)
    tortuga.write("x+")
    tortuga.goto(-screensize,0)

def ybar(tortuga,screensize):
    tortuga.penup()
    tortuga.goto(-screensize,0)
    tortuga.pendown()
    tortuga.left(90)
    tortuga.backward(screensize-90)
    tortuga.forward((screensize-90)*2)
    tortuga.right(90)
    tortuga.write("y+")
    tortuga.goto(-screensize,0)


#FIGURAS#

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
    t.circle(radio)


def dot(size,t):
    t.dot(size, color="red")


def pantalla():
    # Set up the screen
    turtle.tracer(False)
    turtle.update()
    turtle.color("#D3D3D3")
    screensize = 300
    actualscreen = 800 #resolucion de la pantalla

    draw_grid(step=10, size = actualscreen)

    # Hide the turtle and display the result

    # decision = input("Desea continuar")
    #Punto de reflexion

    #Tortuga para dibujar

    turtle.tracer(True)
    turtle.update()

    tortugagrid = turtle.Turtle()
    tortugagrid.shape("arrow")
    tortugagrid.color("blue")
    tortugagrid.shapesize(0.25,0.5,0.5)
    tortugagrid.speed(0)
    mainpos(tortugagrid,screensize)
    xbar(tortugagrid,screensize)
    ybar(tortugagrid,screensize)

# figuras = turtle.Turtle()
# 
# 
# decision = input("Desea continuar")