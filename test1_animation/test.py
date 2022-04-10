# Importing Packages
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# Time Array
t = np.linspace(0, 20, 100)

# Position Arrays
x = np.sin(np.pi/5 * t)
y = np.sin(np.pi/3 * t)

# Setting up Data Set for Animation
dataSet = np.array([x, y])  # Combining our position coordinates
numDataPoints = len(t)


def animate_func(num):
    ax.clear()  # Clears the figure to update the line, point,
    # title, and axes
    # Updating Trajectory Line (num+1 due to Python indexing)
    ax.plot(dataSet[0, :num+1], dataSet[1, :num+1], c='blue')
    # Updating Point Location
    ax.scatter(dataSet[0, num], dataSet[1, num], c='blue', marker='o')
    # Adding Constant Origin
    ax.plot(dataSet[0, 0], dataSet[1, 0], c='black', marker='o')
    # Setting Axes Limits
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])

    # Adding Figure Labels
    ax.set_title('Trajectory \nTime = ' + str(np.round(t[num],
                                                       decimals=2)) + ' sec')
    ax.set_xlabel('x')
    ax.set_ylabel('y')


# Plotting the Animation
fig = plt.figure()
ax = plt.axes()
line_ani = animation.FuncAnimation(fig, animate_func, interval=100,
                                   frames=numDataPoints)
plt.show()
