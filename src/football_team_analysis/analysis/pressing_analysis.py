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


def defensive_analysis_combined(dataframe, season):
    """
    Plot combined defensive analysis for a DataFrame using Seaborn.

    Parameters:
    - dataframe: Pandas DataFrame to be plotted.

    Returns:
    - None (displays the plot).
    """
    sns.set_theme(style="whitegrid", color_codes=True)

    # Create a single scatter plot with different colors for each variable
    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        x="Squad", y="Tkl", data=dataframe, label="Zweikämpfe", color="blue"
    )
    sns.scatterplot(
        x="Squad",
        y="TklW",
        data=dataframe,
        label="Gewonnene Zweikämpfe",
        color="orange",
    )

    plt.title(f"Defensive Analyse - Zweikämpfe vs Gewonnene Zweikämpfe Saison {season}")
    plt.xlabel("Team")
    plt.xticks(rotation=80)
    plt.ylabel("Anzahl der Zweikämpfe / gewonnenen Zweikämpfe")

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()


def ball_recoveries_sbs(dataframe1, dataframe2, season1, season2):
    """
    Plot ball recoveries for two DataFrames side by side using Seaborn.

    Parameters:
    - dataframe1, dataframe2: Pandas DataFrames to be plotted.

    Returns:
    - None (displays the plots).
    """
    sns.set_theme(style="whitegrid", color_codes=True)

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plotting for the first DataFrame
    ax1 = sns.barplot(
        x="Squad", y="Recov", data=dataframe1, palette="rocket", ax=axes[0]
    )
    ax1.set_xlabel("Team")
    ax1.set_ylabel("Anzahl der Balleroberungen")
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=75)
    ax1.set_title(f"Balleroberungen - Saison {season1}")

    # Highlight a specific team in the first plot
    ax1.patches[3].set_facecolor("red")

    # Plotting for the second DataFrame
    ax2 = sns.barplot(
        x="Squad", y="Recov", data=dataframe2, palette="rocket", ax=axes[1]
    )
    ax2.set_xlabel("Team")
    ax2.set_ylabel("")
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=75)
    ax2.set_title(f"Balleroberungen - Saison {season2}")

    # Highlight a specific team in the second plot
    ax2.patches[10].set_facecolor("red")

    # Adjust layout
    plt.tight_layout()

    # Show the plots
    plt.show()


def ball_recoveries_compared(dataframe1, dataframe2):
    """
    Plot combined ball recoveries for two DataFrames using Seaborn.

    Parameters:
    - dataframe1, dataframe2: Pandas DataFrames to be combined and plotted.

    Returns:
    - None (displays the plot).
    """
    sns.set_theme(style="whitegrid", color_codes=True)

    # Combine DataFrames
    combined_df = pd.concat(
        [
            dataframe1.assign(dataset="DataFrame 1"),
            dataframe2.assign(dataset="DataFrame 2"),
        ]
    )

    # Create a single bar plot with hue
    plt.figure(figsize=(20, 10))
    ax = sns.barplot(
        x="Squad", y="Recov", hue="dataset", data=combined_df, palette="rocket"
    )

    ax.set_xlabel("Team")
    ax.set_ylabel("Number of ball recoveries")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=75)
    plt.title("Combined Ball Recoveries - DataFrame 1 vs DataFrame 2")

    # Show the plot
    plt.show()


# Check if there is at least one DataFrame in the list
if data_2022:
    # Access the second DataFrame in the list (index 1) and plot its histogram
    defensive_df1 = data_2022[4]
    defensive_df1 = sorting_data.sort_dataframe_by_column(defensive_df1, "Tkl")

    defensive_df2 = data_2023[4]
    defensive_df2 = sorting_data.sort_dataframe_by_column(defensive_df2, "Tkl")

    ball_recoveries_df1 = data_2022[1]
    ball_recoveries_df1 = sorting_data.sort_dataframe_by_column(
        ball_recoveries_df1, "Recov"
    )
    ball_recoveries_df2 = data_2023[1]
    ball_recoveries_df2 = sorting_data.sort_dataframe_by_column(
        ball_recoveries_df2, "Recov"
    )
    # sns_defensive_analyis(defensive_df)
    ball_recoveries_sbs(ball_recoveries_df1, ball_recoveries_df2, "2022/23", "2023/24")
    # defensive_analysis_combined(defensive_df1, "2022/23")
    # defensive_analysis_combined(defensive_df2, "2023/24")
else:
    print("No DataFrames loaded.")
