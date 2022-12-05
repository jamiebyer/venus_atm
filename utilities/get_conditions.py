import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_AM = pd.read_csv("./data/temp_AM.csv")
df_PM = pd.read_csv("./data/temp_PM.csv")

def get_initial_conditions():
    pass

def get_temperature(altitude):
    temp_AM = np.interp(altitude, df_AM["Alt AM (km)"], df_AM["Temp AM (K)"])
    temp_PM = np.interp(altitude, df_PM["Alt PM (km)"], df_PM["Temp PM (K)"])

    return (temp_AM + temp_PM)/2

plt.plot(df_AM["Temp AM (K)"], df_AM["Alt AM (km)"])
plt.plot(df_PM["Temp PM (K)"], df_PM["Alt PM (km)"])
plt.show()

alts = np.linspace(80, 200)
plt.plot(get_temperature(alts), alts)
plt.show()