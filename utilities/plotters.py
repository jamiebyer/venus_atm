import numpy as np
import matplotlib.pyplot as plt
from utilities.monte_carlo import *
from utilities.constants import *

def plot_cod():
    cods = []
    for i in np.arange(200):
        position, cod = launch_particle()
        cods.append(cod)
        plt.plot(position)

    unique, counts = np.unique(cods, return_counts=True)
    plt.title(unique[0] + ": " + str(counts[0]) + ", " + unique[1] + ": " + str(counts[1]))

    plt.ylabel("radius(m)")
    plt.xlabel("time (s)")
    plt.show()
