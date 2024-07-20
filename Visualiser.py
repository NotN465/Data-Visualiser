from tkinter import *

import customtkinter
from customtkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.figure

class Graphs():
    def __init__(self):
        self.x = []
        self.y = []
    def values(self):
        user_input = entry.get()
        try:
            user_input = float(user_input)
            print(f'You added {user_input} to the x value')
            self.x.append(user_input)
            entry.delete(0, customtkinter.END)
            print(self.x)
        except ValueError:
            print("Invalid input. Please enter a number.")
            user_input = 0
        user_input = entry2.get()
        try:
            user_input = float(user_input)
            print(f'You added {user_input} to the y value')
            self.y.append(user_input)
            entry2.delete(0, customtkinter.END)
            print(self.y)
        except ValueError:
            print("Invalid input. Please enter a number.")
            user_input = 0

    def confirm_input(self):
        self.plot()
    def plot(self):
        ax.clear()
        print()
        ax.plot(self.x, self.y)
        canvas.draw()

root = customtkinter.CTk()
g = Graphs()
root.geometry("1000x1000")

label = CTkLabel(root, text="Hello World")
label.pack()

CTkButton(root, text="Graph", command=g.plot).pack(pady=10)

entry = CTkEntry(root, placeholder_text="Enter value x")
entry.pack(pady=5)
entry2 = CTkEntry(root, placeholder_text="Enter value y")
entry2.pack(pady=5)

xvalue = CTkButton(root, text="Confirm Input", command=g.values)
xvalue.pack(pady=10)

fig = matplotlib.figure.Figure()
ax = fig.add_subplot()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
root.mainloop()