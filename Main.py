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

def do_stuff():
    my_lovely_turtle.goto(-600,-600)


def press():
    do_stuff()
    
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
figura = print("¿Qué figura desea usar?\n\n1: Cono\n2: Tronco de cono\n3: Hemisferio\n")



while ejecucion:
    Opcion = input("Opción: ")
    
    if Opcion == "1":
        
        pr.pantalla()
        
    if Opcion == "2":
        pr.pantalla()
    
    if Opcion == "3":
        pr.pantalla()
    
    

