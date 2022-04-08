from math import sin, cos, pi, exp
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from aero import checkRe


#define problem dimensions, these need to be in the SI
L = 0.050           #semi-hegth
alpha = 1           #wavenumber
lam = 2*pi*L        #wavelength
Red = 10000         #design Reynolds
nu = 5*10**(-6)     #viscosity
U = 0.17            #velocity

#the function checkRe is defined in the aero file, the arguments need to be strictly in this order
Re, U, L, nu = checkRe(Red, U, 2*L, nu)
L = L/2


cr = []
ci = []
#imports the eigenvalues in two arrays, one for the real component and one for the imaginary one
with open('/home/simone/matlab_projects/stabilità/mat.csv',) as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        cr.append(complex(row[0]))
        ci.append(complex(row[1]))

#now we create two arrays, one for time and one for space, both of length k
k = 1001
t = np.linspace(0, 12*pi, k).astype('complex')
x = np.linspace(0, 30*L, k).astype('complex')


#now we should evaluate the solution for each eigenvalue
#the solution is exp(i*alpha*t)*exp(i*alpha*cr)*exp(alpha*ci)

solt = np.empty([k, 1]).astype('complex')
solx = np.array([k, 1]).astype('complex')
#how many modes would you like to evaluate?
modes = 10

im = 1j #defines the imaginary unit

#fixes a mode, then a position in space, then cycles through time, then a second position is fixed and so on un until th
#e end of the x vector, then switches to the next mode
for o in range(modes):
    for n in range(k):
        for m in range(k):
            solx[m] = exp(alpha*x[n]*im)*exp(t[m]*cr[o]*im)*exp(t[m]*ci[o])


print(solx)




