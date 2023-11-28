import os

import pandas as pd
import requests

stats_index = {
    "team_regular_season": 0,
    "team_standard": 2,
    "team_passing": 10,
    "team_pass_types": 12,
    "team_goal_shot_creation": 14,
    "team_defensive_actions": 16,
    "team_possesion": 18,
    "team_misc": 22,
}


def get_stats_from_url(url, stat_type):
    """
    Retrieves team statistics from a given URL.

    Args:
        url (str): The URL to scrape the data from.
        stat_type (str): The type of statistics to retrieve.

    Returns:
        pandas.DataFrame: The DataFrame containing the team statistics.
    """
    response = requests.get(url).text.replace("<!--", "").replace("-->", "")
    index = stats_index[stat_type]
    header = 1 if index != 0 else 0

    df = pd.read_html(response, header=header)[index]
    return df


def fetch_data_to_csv(url, year):
    """
    Fetches data from a given URL and saves it to CSV files.

    Args:
        url (str): The URL to fetch the data from.
        year (int): The year associated with the data.

    Returns:
        None
    """
    df = {}

    for stat_type in stats_index:
        df[stat_type] = get_stats_from_url(url, stat_type=stat_type)

    # Create a directory to store the data
    directory = f"data/raw_data/{year}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the Data to a CSV file
    for name, df_data in df.items():
        file_path = os.path.join(directory, f"{name}_{year}.csv")
        try:
            df_data.to_csv(file_path, index=False)
            print(f"DataFrame '{name}' saved as {file_path}")
        except Exception as e:
            print(f"Error Saving DataFrame '{name}' could not be saved as {file_path}")
