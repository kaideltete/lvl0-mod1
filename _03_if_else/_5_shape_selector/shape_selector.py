import turtle
import turtle
from tkinter import messagebox, simpledialog, Tk

from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    my_turtle = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    q1 = simpledialog.askstring(title='?', prompt=" what shape do you want? triangle circle or square.")
    # Draw the shape requested by the user using if-elif-else statements
my_turtle.pendown()

if q1== "square":
    for i in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)


if q1== "circle":
    my_turtle.circle(100)

if q1== "triangle":
    for i in range(3):
        my_turtle.forward(100)
        my_turtle.left(120)


    # Call the turtle .done() method

    my_turtle.done()
