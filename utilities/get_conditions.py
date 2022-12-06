import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utilities.constants import *

df_AM = pd.read_csv("./data/temp_AM.csv")
df_PM = pd.read_csv("./data/temp_PM.csv")

def get_initial_conditions():
    pass

def get_temperature(altitude):
    altitude /= 1000
    temp_AM = np.interp(altitude, df_AM["Alt AM (km)"], df_AM["Temp AM (K)"])
    temp_PM = np.interp(altitude, df_PM["Alt PM (km)"], df_PM["Temp PM (K)"])

    return (temp_AM + temp_PM)/2

def get_scale_height(m, T):
    H = (k*T)/(m*g)
    return H

def get_pressure(altitude):
    p = p_hom*np.exp(-altitude/get_scale_height(m_H, get_temperature(altitude)))
    return p

def get_number_density(altitude):
    N = get_pressure(altitude)/(k*get_temperature(altitude))
    return N

def plot_temp_profile():
    plt.plot(df_AM["Temp AM (K)"], df_AM["Alt AM (km)"])
    plt.plot(df_PM["Temp PM (K)"], df_PM["Alt PM (km)"])
    plt.show()

    alts = np.linspace(80, 200)
    plt.plot(get_temperature(alts), alts)
    plt.show()

def plot_pressure_profile():
    alts = np.linspace(80, 200)
    plt.plot(get_pressure(alts), alts)
    plt.xlabel("pressure (bar)")
    plt.ylabel("altitude (km)")
    plt.title("pressure profile")
    plt.show()

def plot_number_density_profile():
    alts = np.linspace(80, 200)
    plt.plot(get_number_density(alts), alts)
    plt.xlabel("number density (#/m^3)")
    plt.ylabel("altitude (km)")
    plt.title("number density profile")
    plt.show()
