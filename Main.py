# import turtle


# tortugaxy = turtle.Turtle()


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


# k = input("Desea salir?")

import turtle
import tkinter as tk


def do_stuff():
    my_lovely_turtle.goto(-600,-600)


def press():
    do_stuff()


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root)
    canvas.config(width=900, height=800)
    canvas.pack(side=tk.LEFT)
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("cyan")
    button = tk.Button(root, text="Press me", command=press)
    button.pack()
    my_lovely_turtle = turtle.RawTurtle(screen, shape="turtle")
    root.mainloop()
