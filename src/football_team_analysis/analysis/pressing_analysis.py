import football_team_analysis
import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_data
from football_team_analysis import utils
from football_team_analysis.utils import sorting_data

data_2022 = load_data("../../../data/preprocessed_data/2022")
data_2023 = load_data("../../../data/preprocessed_data/2023")


def defensive_analysis(dataframe):
    plt.subplot(2, 2, 1)
    plt.scatter(dataframe['Squad'], dataframe['Tkl'])
    plt.title('Tackles per Team')
    plt.xlabel('Team Name')
    plt.xticks(rotation=80)
    plt.ylabel('Number of tackles')

    plt.subplot(2, 2, 2)
    plt.scatter(dataframe['Squad'], dataframe['TklW'])
    plt.title('Won tackles per Team')
    plt.xlabel('Team')
    plt.xticks(rotation=90)
    plt.ylabel('Number of won tackles')
    
    plt.show()


# Check if there is at least one DataFrame in the list
if data_2022:
    # Access the second DataFrame in the list (index 1) and plot its histogram
    defensive_df = data_2022[6]
    defensive_df = sorting_data.sort_dataframe_by_column(defensive_df, 'Tkl')
    defensive_analysis(defensive_df)
else:
    print("No DataFrames loaded.")

