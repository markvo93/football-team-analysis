import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import football_team_analysis
from football_team_analysis import utils
from football_team_analysis.utils import load_data, sorting_data

data_2022 = load_data.load_data("data/preprocessed_data/2022")
data_2023 = load_data.load_data("data/preprocessed_data/2023")


def tackle_analysis(df1, df2, season1, season2):
    sns.set_theme(style="whitegrid", color_codes=True)

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plotting for the first DataFrame
    ax1 = sns.barplot(x="Squad", y="Tkl", data=df1, palette="rocket", ax=axes[0])
    ax1.set_xlabel("Team")
    ax1.set_ylabel("Anzahl der Zweikämpfe")
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=75)
    ax1.set_title(f"Zweikämpfe - Saison {season1}")

    # Highlight a specific team in the first plot
    ax1.patches[2].set_facecolor("red")

    # Plotting for the second DataFrame
    ax2 = sns.barplot(x="Squad", y="Tkl", data=df2, palette="rocket", ax=axes[1])
    ax2.set_xlabel("Team")
    ax2.set_ylabel("")
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=75)
    ax2.set_title(f"Zweikämpfe - Saison {season2}")

    # Highlight a specific team in the second plot
    ax2.patches[1].set_facecolor("red")

    # Adjust layout
    plt.tight_layout()

    # Show the plots
    plt.show()

    sns.set_theme(style="whitegrid", color_codes=True)

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plotting for the first DataFrame
    ax1 = sns.scatterplot(x="Squad", y="TklW%", data=df1, palette="rocket", ax=axes[0])
    ax1.set_xlabel("Team")
    ax1.set_ylabel("Prozent")
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=75)
    ax1.set_title(f"Anzahl der gewonnen Zweikämpfe in % {season1}")

    # Highlight a specific team in the first plot
    # ax1.patches[2].set_facecolor("red")

    # Plotting for the second DataFrame
    ax2 = sns.scatterplot(x="Squad", y="TklW", data=df2, palette="rocket", ax=axes[1])
    ax2.set_xlabel("Team")
    ax2.set_ylabel("")
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=75)
    ax2.set_title(f"Zweikämpfe - Saison {season2}")

    # Highlight a specific team in the second plot
    # ax2.patches[1].set_facecolor("red")

    # Adjust layout
    plt.tight_layout()

    # Show the plots
    plt.show()


def tackles_won__percentage_compared(dataframe1, dataframe2):
    sns.set_theme(style="whitegrid", color_codes=True)

    # Combine DataFrames
    combined_df = pd.concat(
        [
            dataframe1.assign(dataset="2022/2023"),
            dataframe2.assign(dataset="2023/2024"),
        ]
    )

    # Create a single bar plot with hue
    plt.figure(figsize=(20, 10))
    ax = sns.barplot(
        x="Squad", y="TklW%", hue="dataset", data=combined_df, palette="muted"
    )

    ax.set_xlabel("Team")
    ax.set_ylabel("Proznet der gewonnenen Zweikämpfe")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=75)
    ax.set_ylim(0, 100)
    ax.legend(title="Saison", loc="upper right")
    plt.title("Vergleich Anzahl der gewonnen Zweikämpfe in %")

    # Show the plot
    plt.show()


def tackels_vs_tackles_won_analysis(df, season):
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
    sns.scatterplot(x="Squad", y="Tkl", data=df, label="Zweikämpfe", color="blue")
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


def ball_recoveries_analysis(df1, df2, season1, season2):
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
    ax1 = sns.barplot(x="Squad", y="Recov", data=df1, palette="rocket", ax=axes[0])
    ax1.set_xlabel("Team")
    ax1.set_ylabel("Anzahl der Balleroberungen")
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=75)
    ax1.set_title(f"Balleroberungen - Saison {season1}")

    # Highlight a specific team in the first plot
    ax1.patches[3].set_facecolor("red")

    # Plotting for the second DataFrame
    ax2 = sns.barplot(x="Squad", y="Recov", data=df2, palette="rocket", ax=axes[1])
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
            dataframe1.assign(dataset="2022/2023"),
            dataframe2.assign(dataset="2023/2024"),
        ]
    )

    # Create a single bar plot with hue
    plt.figure(figsize=(20, 10))
    ax = sns.barplot(
        x="Squad", y="Recov", hue="dataset", data=combined_df, palette="rocket"
    )

    ax.set_xlabel("Team")
    ax.set_ylabel("Anzahl der Balleroberungen")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=75)
    ax.legend(title="Saison", loc="upper right")
    plt.title("Vergleich der Balleroberungen")

    # Show the plot
    plt.show()


# Check if there is at least one DataFrame in the list
if data_2022:
    # Access the second DataFrame in the list (index 1) and plot its histogram
    defensive_df1 = data_2022[5]
    defensive_df1 = sorting_data.sort_dataframe_by_column(defensive_df1, "Tkl")

    defensive_df2 = data_2023[5]
    defensive_df2 = sorting_data.sort_dataframe_by_column(defensive_df2, "Tkl")

    ball_recoveries_df1 = data_2022[1]
    ball_recoveries_df1 = sorting_data.sort_dataframe_by_column(
        ball_recoveries_df1, "Recov"
    )
    ball_recoveries_df2 = data_2023[1]
    ball_recoveries_df2 = sorting_data.sort_dataframe_by_column(
        ball_recoveries_df2, "Recov"
    )

    tackles_in_percent_df1 = data_2022[6]
    tackles_in_percent_df1 = sorting_data.sort_dataframe_by_column(
        tackles_in_percent_df1, "TklW%"
    )

    tackles_in_percent_df2 = data_2023[6]
    tackles_in_percent_df2 = sorting_data.sort_dataframe_by_column(
        tackles_in_percent_df2, "TklW%"
    )

    # ball_recoveries_analysis(
    #    ball_recoveries_df1, ball_recoveries_df2, "2022/23", "2023/24")
    # tackle_analysis(defensive_df1, defensive_df2, "2022/23", "2023/24")
    # ball_recoveries_compared(ball_recoveries_df1, ball_recoveries_df2)
    tackles_won__percentage_compared(tackles_in_percent_df1, tackles_in_percent_df2)
else:
    print("No DataFrames loaded.")
