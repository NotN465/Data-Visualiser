from tkinter import *

import customtkinter
from customtkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.figure
import re

class Graphs():
    def __init__(self):
        self.x = []
        self.y = []
    def values(self):
        user_inputx = entry.get()
        user_inputy = entry2.get()
        float_pattern = re.compile(r'^-?\d+(\.\d+)?$')
        if bool(float_pattern.match(user_inputx)) == True or user_inputx.isdigit() == True:
            user_inputx = float(user_inputx)
            print(f'You added {user_inputx} to the x value')
            self.x.append(user_inputx)
            entry.delete(0, customtkinter.END)
            print(self.x)
        elif bool(float_pattern.match(user_inputx)) == False:
            print("Not a float")
        if bool(float_pattern.match(user_inputy)) == True or user_inputy.isdigit() == True:
            user_inputy = float(user_inputy)
            print(f'You added {user_inputy} to the y value')
            self.y.append(user_inputy)
            entry2.delete(0, customtkinter.END)
            print(self.y)
        elif bool(float_pattern.match(user_inputy)) == False:
            print("Not a float")

    def confirm_input(self):
        self.plot()
    def plot(self):
        ax.clear()
        if len(self.x) == len(self.y):
            ax.plot(self.x, self.y)
            canvas.draw()
        else:
            print("x and y are not the same length")
    def pie_chart(self):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

        label=[i for i in range(len(self.x))]
        print(label)

        labelx = CTkLabel(root, text="X")
        labely = CTkLabel(root, text="Y")

        labelx.pack()
        ax1.pie(self.x,labels=label)
        labely.pack()
        ax2.pie(self.y,labels=label)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack()
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

Button(root, text="Pie Chart", command=g.pie_chart).pack(pady=10)

fig = matplotlib.figure.Figure()
ax = fig.add_subplot()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
root.mainloop()