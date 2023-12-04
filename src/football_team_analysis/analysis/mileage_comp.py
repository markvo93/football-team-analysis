import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import football_team_analysis
from football_team_analysis import utils
from football_team_analysis.utils import load_data, sorting_data

# load csv files into a pd df
data1 = load_data.load_data("data/preprocessed_data/2022")
data2 = load_data.load_data("data/preprocessed_data/2023")


def mileage_compared(df1, df2, season1, season2):
    for df in [df1, df2]:
        if "km/perG" in df.columns:
            df["km/perG"] = df["km/perG"] / 100
        else:
            print(f"There is no column called 'Km' in DataFrame {df}")

    sns.set_theme(style="whitegrid", color_codes=True)

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plotting for the first DataFrame
    ax1 = sns.barplot(x="km/perG", y="Squad", data=df1, palette="rocket", ax=axes[0])
    ax1.set_xlabel("Anzahl Kilometer pro Spiel")
    ax1.set_ylabel("Teams")
    ax1.set_xticklabels(ax1.get_xticklabels())
    ax1.set_title(f"Laufleistung pro Spiel - Saison {season1}")

    # Highlight a specific team in the first plot
    # ax1.patches[0].set_facecolor("red")

    # Plotting for the second DataFrame
    ax2 = sns.barplot(x="km/perG", y="Squad", data=df2, palette="rocket", ax=axes[1])
    ax2.set_xlabel("Anzahl Kilometer pro Spiel")
    ax2.set_ylabel("")
    ax2.set_xticklabels(ax2.get_xticklabels())
    ax2.set_title(f"Laufleistung- Saison {season2}")

    # Highlight a specific team in the second plot
    # ax2.patches[1].set_facecolor("red")

    # Adjust layout
    plt.tight_layout()

    # Show the plots
    plt.show()


# Check if there is at least one DataFrame in the list
# if data_2022:
# Access the second DataFrame in the list (index 1) and plot its histogram
df1 = data1[2]
df2 = data2[2]


df1 = sorting_data.sort_dataframe_by_column(df1, "Km")
df2 = sorting_data.sort_dataframe_by_column(df2, "Km")

mileage_compared(df1, df2, 2022, 2023)
