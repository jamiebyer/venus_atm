import random
from utilities.constants import *
import numpy as np
import matplotlib.pyplot as plt

def dT_dt(t, T, t_max):

    dT_dt = ((1/rho_c_Z) * (gamma*(1-alpha_sky)*(1-alpha)*S_0 - transmissivity*SB*(T**4)) 
    + np.pad((1/(a[1:-1]*A_E*rho_c_Z[1:-1])), (1, 1)) * np.pad((-L[0:-1]*k[0:-1]*(T[1:-1] - T[0:-2]) + L[1:]*k[1:]*(T[2:] - T[1:-1])), (1, 1)))

    return dT_dt

def launch_particle():
    position = []
    max_dt = 10

    s = np.array([0, 0, 0])
    while np.count_nonzero(s) == 0:
        s = np.random.normal(size=3)

    x = r_hom*(s/np.linalg.norm(s))
    v = get_velocity(m_H, T_hom)
    
    snaps = []

    alive = True
    while alive:
        r = np.sqrt(np.sum(x**2))
        position.append(r-r_V)
        g_vec = -(x/np.sqrt(np.sum(x**2)))*G*m_V/(r**2)

        t_snap = get_snap_time()
        dt = min([max_dt, t_snap])

        if dt == t_snap:
            snaps.append(r)

        v += g_vec*dt
        x += v*dt

        if (r < r_V):
            cod = "smash"
            alive = False
        elif (r > r_exo):
            cod = "escape"
            alive = False
    
    return position, cod, snaps

def t_snap_distribution(t_snap):
    T_s = 500 # average lifetime
    return (1/T_s)*np.exp(-t_snap/T_s)

def get_snap_time():
    t_snap = np.linspace(0, 5000, 5000)
    probs = t_snap_distribution(t_snap)

    out_t_snap = random.choices(t_snap, probs, k=1)
    return out_t_snap[0]

def v_distribution(v, m, T):
    return np.sqrt(m/(2*np.pi*k*T))*np.exp(-(m*(v**2))/(2*k*T))

def get_velocity(m, T):
    vels = np.linspace(0, 5000, 5000)
    probs = v_distribution(vels, m, T)

    out_vel = random.choices(vels, probs, k=3)
    return out_vel