# data_processing.py
import pandas as pd
import matplotlib.pyplot as plt

def process_data(sensor_data):
    df = pd.DataFrame(sensor_data)
    summary = df.describe()
    print(summary)
    return df

def plot_data(df):
    df.plot(kind='line')
    plt.show()
