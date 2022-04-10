import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation


def anim_func(num, data_set, t, max_x, max_y, min_y):
    # deletes previous images
    ax.clear()
    # plots the i-esim point
    ax.plot(data_set[0, :num + 1], data_set[1, :num + 1], c='blue')
    # set superior and inferior bounds
    ax.set_xlim(0, max_x)
    ax.set_ylim(min_y, max_y)

    # Adding Figure Labels
    ax.set_title('Waves \nTime = ' + str(np.round(t[num],
                                                  decimals=2)) + ' sec')
    ax.set_xlabel('x')
    ax.set_ylabel('amplitude')


fig = plt.figure()
ax = plt.axes()
line_ani = animation.FuncAnimation(fig, anim_func, interval=1, frames=k)
plt.show()
