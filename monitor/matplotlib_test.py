import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

# Plot Style
plt.style.use('fivethirtyeight')

# Data
x_values = []
y_values = []


index = count()


def animate(i):
    x_values.append(next(index))
    y_values.append((random.randint(0, 5)))
    plt.cla()
    plt.plot(x_values, y_values)


ani = FuncAnimation(plt.gcf(), animate, interval=1)

plt.tight_layout()
plt.show()
