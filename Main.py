# print("Campo Eléctrico para diferentes figuras")


# tortugaxy.setup(600,600)
# tortugaxy.penup()
# tortugaxy.goto(-200,-100)
# tortugaxy.pendown()
# tortugaxy.forward(400)
# tortugaxy.penup()
# tortugaxy.goto(-200,-200)
# tortugaxy.pendown()
# tortugaxy.left(90)
# tortugaxy.forward(400)

import turtle
import tkinter as tk
import pruebas as pr
import Figuras as fig
import CampoElectrico as campo

tortugita = turtle.Turtle()

def do_stuff():
    tortugita.goto(-600,-600)


def press():
    do_stuff()


def fxn(x, y):
  turtle.penup()
  turtle.goto(x, 0)
  turtle.color("blue")
  turtle.write("        "+str(300+x)+","+str(0))
  positionx.append(str(-x))
  positiony.append(str(0))
  pr.dot(20,turtle)
    
# root = tk.Tk()
# canvas = tk.Canvas(root)
# canvas.config(width=900, height=800)
# canvas.pack(side=tk.LEFT)
# screen = turtle.TurtleScreen(canvas)
# screen.bgcolor("cyan")
# button = tk.Button(root, text="Press me", command=press)
# button.pack()
# my_lovely_turtle = turtle.RawTurtle(screen, shape="turtle")
# root.mainloop()

ejecucion = True

positionx = []
positiony = []


while ejecucion:
    figura = print("¿Qué figura desea usar?\n\n1: Cono\n2: Tronco de cono\n3: Hemisferio\n4: Mostrar todas las cordenadas de la carga")
    Opcion = input("Opción: ")
    
    if Opcion == "1":
        radio = input("Radio: ")
        altura = input("Altura: ")
        pr.pantalla()
        fig.cono(int(radio),int(altura),tortugita)
        
    if Opcion == "2":
        radioG = input("Radio Mayor: ")
        radioP = input("Radio Menor: ")
        altura = input("Altura: ")
        pr.pantalla()
        fig.conoTruncado(int(radioG),int(radioP),int(altura),tortugita)
    
    if Opcion == "3":
        radio = input("Radio: ")
        pr.pantalla()
        fig.hemisferio(int(radio),tortugita)

        print("Vamos a poner la carga por favor seleccionar la posicion de la carga")
        wn = turtle.Turtle()
        wn = turtle.Screen()
        wn.onclick(fxn)
        carga = int(input("Por favor ingresar la carga: **Tomar en Cuenta que ya esta en µ**"))
        Celectrico = campo.Chemisferio(int(carga), int(radio),  float(positionx[0]))
        wn.forward(100)
    
    



    
    

