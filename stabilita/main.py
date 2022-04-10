import csv
import numpy as np
from aero_funcs import checkRe
import matplotlib.pyplot as plt
from matplotlib import animation


# define problem parameters, these need to be in the SI
L = 0.050  # semi-height
alpha = 1  # wave-number
lam = 2 * np.pi * L  # wavelength
Red = 10000  # design Reynolds
nu = 5 * 10 ** (-6)  # viscosity
U = 0.17  # velocity

# the function checkRe is defined in the aero file, the arguments need to be strictly in this order
# Re, U, L, nu = checkRe(Red, U, 2 * L, nu)
# L = L / 2

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
max_X = 30*L  # how much of the pipe we want to visualize
t_real = np.linspace(0, 12 * np.pi, k)
t = t_real.astype('complex')
x = np.linspace(0, max_X, k).astype('complex')

# now we should evaluate the solution for each eigenvalue
# the solution is exp(i*alpha*x)*exp(i*t*cr)*exp(t*ci)
im = 1j  # defines the imaginary unit because python is dumb sometimes

o = 9

# sol = np.exp(im*alpha*x)*np.exp(im*t*cr[o])*np.exp(t*ci[o])


# these are needed purely for aesthetic reasons, to determine the y-axis
# max_Y = max(sol)
# min_Y = min(sol)

# dataSet = np.array([x, sol])


# def anim_func(num):
#     # deletes previous images
#     ax.clear()
#     # plots the i-esim point
#     ax.plot(dataSet[0, :num+1], dataSet[1, :num+1], c='blue')
#     # set superior and inferior bounds
#     ax.set_xlim(0, max_X)
#     ax.set_ylim(min_Y, max_Y)

#     # Adding Figure Labels
#     ax.set_title('Waves \nTime = ' + str(np.round(t_real[num],
#                                                   decimals=2)) + ' sec')
#     ax.set_xlabel('x')
#     ax.set_ylabel('amplitude')


# fig = plt.figure()
# ax = plt.axes()
# line_ani = animation.FuncAnimation(fig, anim_func, interval=1, frames=k)
# plt.show()

# generates a matrix in which each row is a solution with a different mode
sol = np.empty([len(cr), k]).astype('complex')
for i in range(len(cr)):
    sol[i, :] = np.genfromtxt(f'sol/sol{i}.csv', delimiter=',', dtype=str)
    sol[i, :] = np.complex_(sol[i, :])

print(type(sol), len(sol))

import time

for i in range(k):
    print(sol[1, i])
    time.sleep(0.5)