"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':



    messagebox.showinfo(message="give 2 numbers to add")

    q1 = simpledialog.askstring(title='math 1', prompt="give the first number")

    q2 = simpledialog.askstring(title='math 1', prompt="give the second number")

    ans=int(q1)+int(q2)

    messagebox.showinfo(message=str(ans))






