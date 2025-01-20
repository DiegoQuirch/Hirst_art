from random import choice
from get_colors import colors_list
import turtle as t

t.colormode(255)
screen = t.Screen()
screen.setup(width=600)  # Adjust the screen width
turtle = t.Turtle()
turtle.speed("fastest")
turtle.hideturtle()

# Set the starting position
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

def draw_dot():
    turtle.penup()
    turtle.dot(20, choice(colors_list))
    
def draw_row():
    for _ in range(10):
        draw_dot()
        turtle.forward(50)

def draw_hirst():

    for _ in range(10):
        draw_row()
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

draw_hirst()
screen.exitonclick()

