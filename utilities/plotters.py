import numpy as np
import matplotlib.pyplot as plt
from utilities.monte_carlo import *
from utilities.constants import *
from utilities.get_conditions import write_species_properties

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
    for i in np.arange(50):
        position, _, cod, _, _, _ = launch_particle()
        cods.append(cod)
        plt.plot(position)

    unique, counts = np.unique(cods, return_counts=True)
    if (len(unique) > 1):
        plt.title(unique[0] + ": " + str(counts[0]) + ", " + unique[1] + ": " + str(counts[1]))

    plt.ylabel("radius(m)")
    plt.xlabel("time (s)")
    plt.show()

def plot_velocity():
    for i in np.arange(200):
        _, velocity, _, _, _, _ = launch_particle()
        plt.plot(velocity)

    plt.ylabel("velocity")
    plt.xlabel("time (s)")
    plt.show()

def plot_velocity_hist():
    full_snaps = []
    for i in np.arange(200):
        _, _, _, snaps_vel, _ = launch_particle()
        full_snaps += snaps_vel

    full_snaps = np.array(full_snaps)

    plt.hist(full_snaps)
    plt.xlabel("velocity")
    plt.show()

def plot_collision_distribution():

    for altitude in np.linspace(1, 6E5, 10):
        for v in np.linspace(1000, 7000, 7):
            v = 2000
            t_collision = np.linspace(0, 5000, 5000)
            probs = t_collision_distribution(t_collision, altitude, v)

            plt.plot(t_collision, probs)

    plt.show()

def plot_number_density_profile():
    write_species_properties()
    #number_density = write_number_density()
    #plt.plot(number_density)
    #plt.show()