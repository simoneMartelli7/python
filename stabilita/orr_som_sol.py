import numpy as np
import csv
from os import system
# from main import k, max_X, alpha
# this script generates each solution and then dumps it into a series of csv files which can then be read from another
# script
L = 0.050
alpha = 1
#
cr = []
ci = []
# # imports the eigenvalues in two arrays, one for the real component and one for the imaginary one
with open('mat.csv', ) as eigenvals:
    csvReader = csv.reader(eigenvals)
    for row in csvReader:
        cr.append(complex(row[0]))
        ci.append(complex(row[1]))
#
# # now we create two arrays, one for time and one for space, both of length k
k = 1001
max_X = 50*L  # how much of the pipe we want to visualize
t = np.linspace(0, 5 * np.pi, k).astype('complex')
x = np.linspace(0, max_X, k).astype('complex')

# now we should evaluate the solution for each eigenvalue
# the solution is exp(i*alpha*x)*exp(i*t*cr)*exp(t*ci)
im = 1j  # defines the imaginary unit because python is dumb sometimes

system('rm -rf sol/*')
for o in range(len(cr)):
    sol = np.exp(im*alpha*x)*np.exp(im*t*cr[o])*np.exp(t*ci[o])
    system(f'touch sol/sol{o}.csv')
    np.savetxt(f'sol/sol{o}.csv', sol, delimiter=',')
