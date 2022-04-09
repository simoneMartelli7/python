from math import pi, exp
import csv
import numpy as np
from aero_funcs import checkRe
from anim_funcs import create_gif  # , animate, counter

# define problem dimensions, these need to be in the SI
L = 0.050  # semi-hegth
alpha = 1  # wavenumber
lam = 2 * pi * L  # wavelength
Red = 10000  # design Reynolds
nu = 5 * 10 ** (-6)  # viscosity
U = 0.17  # velocity

# the function checkRe is defined in the aero file, the arguments need to be strictly in this order
Re, U, L, nu = checkRe(Red, U, 2 * L, nu)
L = L / 2

cr = []
ci = []
# imports the eigenvalues in two arrays, one for the real component and one for the imaginary one
with open('mat.csv', ) as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        cr.append(complex(row[0]))
        ci.append(complex(row[1]))

# now we create two arrays, one for time and one for space, both of length k
k = 1001
t = np.linspace(0, 12 * pi, k).astype('complex')
x = np.linspace(0, 30 * L, k).astype('complex')

# now we should evaluate the solution for each eigenvalue
# the solution is exp(i*alpha*t)*exp(i*alpha*cr)*exp(alpha*ci)

solt = np.empty_like(t)
solx = np.empty_like(t)
# how many modes would you like to evaluate?
modes = 10

im = 1j  # defines the imaginary unit because python is dumb sometimes

# fixes a mode, then a position in space, then cycles through time, then a second position is fixed and so on un until
# the end of the x vector, then switches to the next mode
# testing with a single mode
o = 2
for n in range(k):
    for m in range(k):
        solx[m] = exp(alpha * x[n] * im) * exp(t[m] * cr[o] * im) * exp(t[m] * ci[o])

create_gif(x, solx)
