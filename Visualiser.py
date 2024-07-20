from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.figure
class Graphs():
    def __init__(self):
        self.x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.y = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
    def plot(self):
        ax.clear()
        print()
        ax.plot(self.x, self.y)
        canvas.draw()

root = Tk()
g = Graphs()
root.geometry("500x500")
label = Label(root, text="Hello World")
label.pack()
Button(root, text="Graph", command=g.plot).pack(pady=10)

fig = matplotlib.figure.Figure()
ax = fig.add_subplot()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
root.mainloop()