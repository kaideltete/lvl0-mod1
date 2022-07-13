import turtle
from tkinter import messagebox, simpledialog, Tk
import math

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    my_turtle = turtle.Turtle()

    q1 = simpledialog.askstring(title='', prompt=" rad (radius)  or cer (Circumference)")



    my_turtle.penup()

    my_turtle.goto(100,100)
    my_turtle.pendown()


    if q1=="rad":
        rad = simpledialog.askstring(title='', prompt="enter a radius")
        my_turtle.circle(int(rad))
        area=math.pi*int(rad)*int(rad)
        my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
        my_turtle.penup()
        my_turtle.hideturtle()



    if q1=="cer":
        cer = simpledialog.askstring(title='', prompt="enter a Circumference")
        my_turtle.circle(int(cer))
        cer=2*math.pi*int(cer)
        my_turtle.write(arg="area = " + str(cer), move=True, align='left', font=('Arial',8,'normal'))
        my_turtle.penup()
        my_turtle.hideturtle()








    my_turtle.hideturtle()

    turtle.done()
# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
