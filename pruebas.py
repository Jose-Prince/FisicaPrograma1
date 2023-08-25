import turtle

def draw_grid(step):
    for i in range(-250, 251, step):
        turtle.penup()
        turtle.goto(i, -250)
        turtle.pendown()
        turtle.goto(i, 250)
        
    for i in range(-250, 251, step):
        turtle.penup()
        turtle.goto(-250, i)
        turtle.pendown()
        turtle.goto(250, i)

# Set up the screen
screen = turtle.Screen()
turtle.tracer(False)
turtle.update()
# Create a turtle
grid_turtle = turtle.Turtle()
grid_turtle.penup()
grid_turtle.goto(0, 0)
grid_turtle.pendown()

draw_grid(step=10)

# Hide the turtle and display the result
grid_turtle.hideturtle()
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