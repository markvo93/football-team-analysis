import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import football_team_analysis
from football_team_analysis import utils
from football_team_analysis.utils import load_data, sorting_data

data_2022 = load_data.load_data("data/preprocessed_data/2022")
data_2023 = load_data.load_data("data/preprocessed_data/2023")


def crosses_analysis(df1, df2, season1, season2):
    sns.set_theme(style="whitegrid", color_codes=True)

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plotting for the first DataFrame
    ax1 = sns.barplot(x="Squad", y="Crs", data=df1, palette="rocket", ax=axes[0])
    ax1.set_xlabel("Team")
    ax1.set_ylabel("Anzahl")
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=75)
    ax1.set_title(f"Anzahl der Flanken - Saison {season1}")

    # Highlight a specific team in the first plot
    ax1.patches[0].set_facecolor("red")

    # Plotting for the second DataFrame
    ax2 = sns.barplot(x="Squad", y="Crs", data=df2, palette="rocket", ax=axes[1])
    ax2.set_xlabel("Team")
    ax2.set_ylabel("")
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=75)
    ax2.set_title(f"Anzahl der Flanken - Saison {season2}")

    # Highlight a specific team in the second plot
    ax2.patches[1].set_facecolor("red")

    # Adjust layout
    plt.tight_layout()

    # Show the plots
    plt.show()


# Check if there is at least one DataFrame in the list
if data_2022:
    # Access the second DataFrame in the list (index 1) and plot its histogram
    crosses_df_22 = data_2022[0]
    crosses_df_23 = data_2023[0]

    crosses_df_22 = sorting_data.sort_dataframe_by_column(crosses_df_22, "Crs")
    crosses_df_23 = sorting_data.sort_dataframe_by_column(crosses_df_23, "Crs")
    crosses_analysis(crosses_df_22, crosses_df_23, 2022, 2023)
else:
    print("No DataFrames loaded.")
