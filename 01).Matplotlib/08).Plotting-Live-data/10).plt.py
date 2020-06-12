import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):

    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    #cla to clear the previous plot so that they don't stack on top of each other.
    plt.cla()
    plt.plot(x,y1,label = "channel 1")
    plt.plot(x,y2,label = "channel 2")

    plt.legend(loc = "upper left")
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(),animate, interval = 1000)


plt.tight_layout()
plt.show()
