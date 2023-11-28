import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import football_team_analysis
from football_team_analysis import utils
from football_team_analysis.utils import load_data, sorting_data

data_2022 = load_data.load_data("data/preprocessed_data/2022")
data_2023 = load_data.load_data("data/preprocessed_data/2023")


def defensive_analysis(dataframe):
    plt.subplot(2, 2, 1)
    plt.scatter(dataframe["Squad"], dataframe["Tkl"])
    plt.title("Zweikämpfe")
    plt.xlabel("Teamname")
    plt.xticks(rotation=80)
    plt.ylabel("Anzahl der Zweikämpfe")

    plt.subplot(2, 2, 2)
    plt.scatter(dataframe["Squad"], dataframe["TklW"])
    plt.title("Gewonnene Zweikämpfe")
    plt.xlabel("Teamname")
    plt.xticks(rotation=90)
    plt.ylabel("Nummer der gewonnenen Zweikämpfe")

    plt.show()


def sns_defensive_analyis(dataframe):
    sns.set_theme(style="whitegrid", color_codes=True)
    ax = sns.barplot(x="Squad", y="Tkl", data=dataframe, palette="rocket")
    ax.set_xlabel("Team")
    ax.set_ylabel("Number of tackles")
    plt.xticks(rotation=75)
    plt.rcParams["figure.figsize"] = [20, 10]
    plt.title("Tackles per Team")
    plt.show()


def ball_recoveries(dataframe):
    sns.set_theme(style="whitegrid", color_codes=True)
    ax = sns.barplot(x="Squad", y="Recov", data=dataframe, palette="rocket")
    ax.set_xlabel("Team")
    ax.set_ylabel("Number of ball recoveries")
    plt.xticks(rotation=75)
    plt.rcParams["figure.figsize"] = [20, 10]
    plt.title("Ball recoveries per Team")
    plt.show()


# Check if there is at least one DataFrame in the list
if data_2022:
    # Access the second DataFrame in the list (index 1) and plot its histogram
    defensive_df = data_2022[4]
    defensive_df = sorting_data.sort_dataframe_by_column(defensive_df, "Tkl")

    ball_recoveries_df = data_2022[1]
    ball_recoveries_df = sorting_data.sort_dataframe_by_column(
        ball_recoveries_df, "Recov"
    )
    sns_defensive_analyis(defensive_df)
    ball_recoveries(ball_recoveries_df)
else:
    print("No DataFrames loaded.")
