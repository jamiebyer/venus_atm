import numpy as np
import matplotlib.pyplot as plt
from utilities.monte_carlo import *
from utilities.constants import *

def plot_collisions():
    full_collisions = []
    for i in np.arange(500):
        _, _, _, collisions = launch_particle()
        full_collisions.append(collisions)

    #plt.hist(full_collisions)
    plt.hist(full_collisions, bins=range(min(full_collisions), max(full_collisions) + 1, 1))
    plt.title("collisions")
    plt.xlabel("# collisions")
    plt.ylabel("# particles")
    plt.show()

def plot_r_snaps():
    full_snaps = []
    for i in np.arange(500):
        _, _, snaps = launch_particle()
        full_snaps += snaps

    full_snaps = np.array(full_snaps)

    plt.hist(full_snaps)
    plt.title("distribution of particles by radius (500)")
    plt.xlabel("radius (m)")
    plt.show()

def plot_cod():
    cods = []
    for i in np.arange(5):
        position, cod, _, _ = launch_particle()
        cods.append(cod)
        plt.plot(position)

    unique, counts = np.unique(cods, return_counts=True)
    if (len(unique) > 1):
        plt.title(unique[0] + ": " + str(counts[0]) + ", " + unique[1] + ": " + str(counts[1]))

    plt.ylabel("radius(m)")
    plt.xlabel("time (s)")
    plt.show()

