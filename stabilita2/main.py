from math import exp, sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import count
from aero_func import checkRe
from csv import reader

### defines system parameters
L = 0.050
alpha = 1
lam = 2*pi*L
Red = 10**5
nu = 5*10**(-5)
U = 0.17

Re, U, L, nu = checkRe(Red, U, 2*L, nu)
L = L/2                                     ### for the Reynolds number we need the heigth, while this parameter is the semi-heigth

cr = []
ci = []

with open('mat.csv') as f:
    csvReader = reader(f)
    for row in csvReader:
        cr.append(complex(row[0]))
        ci.append(complex(row[1]))

min_w = float(min(cr))
### the space and time vector are created, both of length k
k = 1001
x = np.linspace(0, 30*L, k)
t = np.linspace(0, 30*pi/min_w, k)





