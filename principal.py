import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas
import pruebas

# def draw_square():
#     turtle.pendown()
#     for _ in range(4):
#         turtle.forward(100)
#         turtle.left(90)
#     turtle.penup()

# root = tk.Tk()
# root.title("Turtle Graphics with Tkinter")

# canvas = ScrolledCanvas(root)
# canvas.pack(fill=tk.BOTH, expand=tk.YES)

# turtle = RawTurtle(canvas)
# turtle.speed(1)  # Set the turtle's drawing speed (1 is slowest, 10 is fastest)

# draw_button = tk.Button(root, text="Draw Square", command= draw_square)
# draw_button.pack()

# root.mainloop()




# figuras = turtle.Turtle()


# root = tk.Tk()
# root.title("Turtle Graphics with Tkinter")

# canvas = ScrolledCanvas(root)
# canvas.pack(fill=tk.BOTH, expand=tk.YES)

# turtles = RawTurtle(canvas)
# turtles.speed(1)  # Set the turtle's drawing speed (1 is slowest, 10 is fastest)

# draw_button = tk.Button(root, text="Draw Square", command= pantalla)
# draw_button.pack()

# root.mainloop()


# import package
import turtle
  
  
# screen object
wn = turtle.Screen()
  
# method to perform action
def fxn(x, y):
  turtle.goto(x, y)
  turtle.write(str(x)+","+str(y))
  pruebas.dot(20,turtle)
  
# onclick action 
wn.onclick(fxn)
wn.mainloop()
 
decision = input("Desea continuar")