"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':

    window = Tk()

    eq = simpledialog.askstring(title='math type', prompt='add,subtract, multiply, or divide?')

    if eq == "add":
        messagebox.showinfo(message="give 2 numbers to add")

        q1 = simpledialog.askstring(title='math 1', prompt='give the first number')

        q2 = simpledialog.askstring(title='math 1', prompt='give the second number')

        ans = int(q1)+int(q2)

        messagebox.showinfo(message=str(ans))

    if eq == "subtract":
        messagebox.showinfo(message="give 2 numbers to subtract")

        q1 = simpledialog.askstring(title='math 1', prompt='give the first number')

        q2 = simpledialog.askstring(title='math 1', prompt='give the second number')

        ans = int(q1)-int(q2)

        messagebox.showinfo(message=str(ans))

    if eq == "multiply":
        messagebox.showinfo(message="give 2 numbers to multiply")

        q1 = simpledialog.askstring(title='math 1', prompt='give the first number')

        q2 = simpledialog.askstring(title='math 1', prompt='give the second number')

        ans = int(q1)*int(q2)

        messagebox.showinfo(message=str(ans))

    if eq == "divide":
        messagebox.showinfo(message="give 2 numbers to divide")

        q1 = simpledialog.askstring(title='math 1', prompt='give the first number')

        q2 = simpledialog.askstring(title='math 1', prompt='give the second number')

        ans = int(q1)/int(q2)

        messagebox.showinfo(message=str(ans))
