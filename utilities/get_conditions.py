import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utilities.constants import *

df_AM = pd.read_csv("./data/temp_AM.csv")
df_PM = pd.read_csv("./data/temp_PM.csv")

def get_temperature(altitude):
    altitude /= 1000.0
    temp_AM = np.interp(altitude, df_AM["Alt AM (km)"], df_AM["Temp AM (K)"])
    temp_PM = np.interp(altitude, df_PM["Alt PM (km)"], df_PM["Temp PM (K)"])

    return (temp_AM + temp_PM)/2

def get_scale_height(m, altitude):
    T = get_temperature(altitude)
    g = (G*m_V)/((altitude+r_V)**2)
    H = (k*T)/(m*g)
    return H

def get_number_density(m, p_0):
    dz = 1
    altitudes = np.arange(r_hom, r_exo, dz, dtype=float) - r_V
    H = get_scale_height(m, altitudes)
    
    integ = np.cumsum((1/H)*dz)

    p = p_0*np.exp(-integ)
    
    N = p/(k*get_temperature(altitudes))
    return N

def write_species_properties():
    cols = ["species", "mass (kg)", "altitude (m)", "mixing ratio", "p0"]
    
    species = ["H", "He", "C", "N", "O", "Ne", "Ar", "Kr", "Xe", "H2", "NH3", "H2O", "HF", "CO",
    "N2", "O2", "H2S", "HCl", "CO2", "SO2", "COS", "H2SO4"]
    
    m = np.array([1.0079, 4.0026, 12.0107, 14.0067, 15.9994, 20.1797, 39.948, 83.898, 131.293, 2.016, 
    17.031, 18.015, 20.006, 28.0101, 28.0134, 31.9988, 34.0809, 36.4609, 44.0095, 64.0638, 
    90.9982, 98.0785])*1.66054e-27
    
    mixing_ratio = np.array([0.5E-6, 4E-6, 0.00965, 0.0145, 0.965, 7E-6, 30E-6, 69E-9, 0.10E-6, 1E-9, 1E-9,
    0.9E-6, 2E-9, 40000E-6, 3.5, 8.6E-6, 1E-9, 0.1E-6, 96.5, 0.1E-6, 1E-9, 1E-9])
    
    p_0 = mixing_ratio*p_hom
    
    number_densities = []
    for i in range(len(species[:4])):
        number_densities.append(get_number_density(m[i], p_0[i]))
        plt.plot(number_densities[i])
    
    plt.legend(species[:4])
    plt.show()
    
    #df.write_csv("./data/number_densities.csv")