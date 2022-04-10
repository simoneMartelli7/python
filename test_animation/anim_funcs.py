import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def _2d_plot(x0, y0):
    plt.plot(x0, y0)
    plt.show()


def animate_func(num, data_set, t):
    ax.clear()  # Clears the figure to update the line, point,
    # title, and axes
    # Updating Trajectory Line (num+1 due to Python indexing)
    ax.plot3D(data_set[0, :num + 1], data_set[1, :num + 1],
              data_set[2, :num + 1], c='blue')
    # Updating Point Location
    ax.scatter(data_set[0, num], data_set[1, num], data_set[2, num],
               c='blue', marker='o')
    # Adding Constant Origin
    ax.plot3D(data_set[0, 0], data_set[1, 0], data_set[2, 0],
              c='black', marker='o')
    # Setting Axes Limits
    ax.set_xlim3d([-1, 1])
    ax.set_ylim3d([-1, 1])
    ax.set_zlim3d([0, 100])

    # Adding Figure Labels
    ax.set_title('Trajectory \nTime = ' + str(np.round(t[num],
                                                       decimals=2)) + ' sec')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')


# Plotting the Animation
fig = plt.figure()
ax = plt.axes(projection='3d')
line_ani = animation.FuncAnimation(fig, animate_func, interval=100,
                                   frames=1001)
plt.show()
