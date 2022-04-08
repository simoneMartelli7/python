import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from itertools import count 
import random 
#from IPython import display 


x = []
y = []
i = count()

def animatej(j):
    x.append(next(i))
    y.append(random.randint(0, 10))
    plt.plot(x, y)

animation_1 = animation.FuncAnimation(plt.gcf(), animatej, interval = 1000)
plt.show()
