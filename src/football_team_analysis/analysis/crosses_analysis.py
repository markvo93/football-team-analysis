import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import football_team_analysis
from football_team_analysis import utils
from football_team_analysis.utils import load_data, sorting_data

data_2022 = load_data.load_data("data/preprocessed_data/2022")
data_2023 = load_data.load_data("data/preprocessed_data/2023")


def crosses_analysis(dataframe):
    sns.set_theme(style="whitegrid", color_codes=True)
    ax = sns.barplot(x="Squad", y="Crs", data=dataframe, palette="rocket")
    ax.set_xlabel("Team")
    ax.set_ylabel("Number of crosses")
    plt.xticks(rotation=75)
    plt.rcParams["figure.figsize"] = [20, 10]
    plt.title("Crosses per Team")
    plt.show()


# Check if there is at least one DataFrame in the list
if data_2022:
    # Access the second DataFrame in the list (index 1) and plot its histogram
    crosses_df_22 = data_2022[0]
    crosses_df_23 = data_2023[0]

    crosses_df_22 = sorting_data.sort_dataframe_by_column(crosses_df_22, "Crs")
    crosses_df_23 = sorting_data.sort_dataframe_by_column(crosses_df_23, "Crs")
    crosses_analysis(crosses_df_22)
    crosses_analysis(crosses_df_23)
else:
    print("No DataFrames loaded.")
