import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import count

counter = count()


def animate(cout, x, solx):

    while next(cout) != 100:   # takes vectors' elements one at a time
        x0 = x[next(cout)]
        # t0 = t[next(counter)]
        s0 = solx[next(cout)]
        # plots the corresponding points
        plt.plot(x0, s0)


def create_gif(x, solx):
    my_writer = animation.FFMpegWriter()
    animate(counter, x, solx)
    # does the actual animation
    animation_0 = animation.FuncAnimation(plt.gcf(), animate, interval=100)
    # show the animation live, can be suppressed if the only intent is saving to a file
    animation_0.save('stabilita.mp4', writer=my_writer, fps=30)
    plt.show()

