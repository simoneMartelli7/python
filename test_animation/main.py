from anim_funcs import _2d_plot, animate_func
from math import sin, pi
import numpy as np

x = np.linspace(0, 20*pi, 1001)
y = []
t = np.linspace(0, 100, 1001)

for i in range(len(x)):
    y.append(sin(x[i]*t[i]))


dataSet = np.array([x, y])

animate_func(0, dataSet, t)
