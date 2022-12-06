import random
from utilities.constants import *
from utilities.get_conditions import *
import numpy as np
import matplotlib.pyplot as plt

def get_escape_velocity(r):
    esc_v = np.sqrt(2*G*m_V/(r-r_V))
    return esc_v

def check_escape(r, v, m, d):
    p = (m*g)/(np.sqrt(2)*np.pi*(d**2))
    if ((np.sum(v**2) > get_escape_velocity(r)) & (np.dot(np.linalg.norm(r), np.linalg.norm(v)) > 0)):
        if (p < get_pressure(r-r_V)):
            return True
    return False

def perform_collision(m1, v1, r):
    m2 = m_H
    v2 = get_velocity(m2, get_temperature(r-r_V))

    p1 = m1*v1
    p2 = m2*v2
    p_final = p1+p2
    v_final = p_final/m1
    return v_final

def launch_particle():
    position = []
    collisions = 0
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
        t_collision = get_collision_time(r-r_V, np.sqrt(np.sum(v**2)))
        dt = min([max_dt, t_snap, t_collision])

        if dt == t_snap:
            snaps.append(r)
        elif dt == t_collision:
            collisions += 1
            v = perform_collision(m_H, v, r)

        v += g_vec*dt
        x += v*dt

        if (r < r_V):
            cod = "smash"
            alive = False
        elif check_escape(r, v, m_H, d_H):
            cod = "escape"
            alive = False
    
    return position, cod, snaps, collisions

def t_snap_distribution(t_snap):
    T_s = 500 # average lifetime
    return (1/T_s)*np.exp(-t_snap/T_s)

def get_snap_time():
    t_snap = np.linspace(0, 5000, 5000)
    probs = t_snap_distribution(t_snap)

    out_t_snap = random.choices(t_snap, probs, k=1)
    return out_t_snap[0]

def t_collision_distribution(t_collision, altitude, v):
    T_c = 1/(sigma_H*get_number_density(altitude)*v)
    return (1/T_c)*np.exp(-t_collision/T_c)

def get_collision_time(altitude, v):
    t_collision = np.linspace(0, 5000, 5000)
    probs = t_collision_distribution(t_collision, altitude, v)

    out_t_collision = random.choices(t_collision, probs, k=1)
    return out_t_collision[0]

def v_distribution(v, m, T):
    return np.sqrt(m/(2*np.pi*k*T))*np.exp(-(m*(v**2))/(2*k*T))

def get_velocity(m, T):
    vels = np.linspace(0, 5000, 5000)
    probs = v_distribution(vels, m, T)

    out_vel = np.array(random.choices(vels, probs, k=3))
    return out_vel