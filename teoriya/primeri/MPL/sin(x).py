import math
import matplotlib.pyplot as plt
import numpy as np



def func(x):
    """
    sinc(x)
    """
    return math.sin(x)


if __name__ == '__main__':
    xmin = -6
    xmax = 6
    ymax = 6
    ymin = -6
    count = 200
    xlist = np.linspace(xmin, xmax, count)
    ylist = [func(x) for x in xlist]
    plt.plot(xlist, ylist)
    plt.grid(True)
    plt.legend()
    plt.show()