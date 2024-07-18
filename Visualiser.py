from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.figure
def plot():
    ax.clear()
    x = np.random.randint(0,10,10)
    y = np.random.randint(0, 10, 10)
    ax.plot(x, y)
    canvas.draw()

root = Tk()
root.geometry("500x500")
label = Label(root, text="Hello World")
label.pack()

Button(root, text="Graph", command=plot).pack(pady=10)

fig = matplotlib.figure.Figure()
ax = fig.add_subplot()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
tooolbar = NavigationToolbar2Tk(canvas, root)
tooolbar.update()
tooolbar.pack(anchor="w",fill=X)
root.mainloop()