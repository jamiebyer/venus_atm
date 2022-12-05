import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import butter, filtfilt


df1 = pd.read_csv("./data/venus-Table1.csv")
df2 = pd.read_csv("./data/venus-Table2.csv")
df3 = pd.read_csv("./data/venus-Table3.csv")
df4 = pd.read_csv("./data/venus-Table4.csv")
df5 = pd.read_csv("./data/venus-Table5.csv")

df = pd.concat([df1, df2, df3, df4, df5], axis=0)

df_AM = df.filter(["Temp AM (K)", "Alt AM (km)"], axis=1)
df_AM.set_index("Alt AM (km)", inplace = True)
df_AM = df_AM.sort_index()
df_AM = df_AM.dropna()

df_PM = df.filter(["Temp PM (K)", "Alt PM (km)"], axis=1)
df_PM.set_index("Alt PM (km)", inplace = True)
df_PM = df_PM.sort_index()
df_PM = df_PM.dropna()

def butter_lowpass_filter(data):
    # Filter requirements.
    T = 1.0         # Sample Period
    fs = 1.0       # sample rate, Hz
    cutoff = 10      # desired cutoff frequency of the filter, Hz , slightly higher than actual 1.2 Hz
    nyq = 0.5 * fs  # Nyquist Frequency
    order = 2       # sin wave can be approx represented as quadratic
    #n = int(T * fs) # total number of samples

    normal_cutoff = cutoff / nyq
    # Get the filter coefficients 
    b, a = butter(order, 0.1, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

def plot_temperature_profile():
    plt.scatter(df["Temp AM (K)"], df["Alt AM (km)"])
    plt.scatter(df["Temp PM (K)"], df["Alt PM (km)"])
    plt.legend("AM", "PM")
    plt.show()

def plot_filter():
    plt.subplot(1, 2, 1)
    y_AM = butter_lowpass_filter(df_AM["Temp AM (K)"])

    plt.scatter(df_AM["Temp AM (K)"], df_AM.index)
    plt.plot(y_AM, df_AM.index, c="orange")

    plt.xlabel("Temp (K)")
    plt.ylabel("Altitude (km)")
    plt.title("Temperature profile, AM")

    plt.subplot(1, 2, 2)
    y_PM = butter_lowpass_filter(df_PM["Temp PM (K)"])

    plt.scatter(df_PM["Temp PM (K)"], df_PM.index)
    plt.plot(y_PM, df_PM.index, c="orange")

    plt.xlabel("Temp (K)")
    plt.ylabel("Altitude (km)")
    plt.title("Temperature profile, PM")
    plt.show()

def save_data():
    df_AM["Temp AM (K)"] = butter_lowpass_filter(df_AM["Temp AM (K)"])
    const_temp_AM = df_AM[df_AM.index > 145]["Temp AM (K)"].mean()
    df_PM["Temp PM (K)"] = butter_lowpass_filter(df_PM["Temp PM (K)"])
    const_temp_PM = df_PM[df_PM.index > 145]["Temp PM (K)"].mean()
    
    df_AM.loc[155] = [const_temp_AM]
    df_AM.loc[300] = [const_temp_AM]
    df_PM.loc[155] = [const_temp_PM]
    df_PM.loc[300] = [const_temp_PM]

    df_AM["Alt AM (km)"] = df_AM.index
    df_PM["Alt PM (km)"] = df_PM.index
    
    df_AM.to_csv("./data/temp_AM.csv")
    df_PM.to_csv("./data/temp_PM.csv")

#save_data()