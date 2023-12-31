import glob

import matplotlib.pyplot as plt
import pandas as pd

import football_team_analysis
from football_team_analysis.utils import load_data

data = load_data.load_data("data/preprocessed_data/2022")


def plot_scatter(dataframe):
    # Simple Visualization: Histogram of values in the first column
    plt.scatter(dataframe["Squad"], dataframe["Pts"])
    plt.title("Scatter of Points")
    plt.xlabel("Team")
    plt.xticks(rotation=90)
    plt.ylabel("Points")
    plt.show()


# Check if there is at least one DataFrame in the list
if data:
    # Access the second DataFrame in the list (index 2) and plot its histogram
    second_dataframe = data[2]
    plot_scatter(second_dataframe)
else:
    print("No DataFrames loaded.")
