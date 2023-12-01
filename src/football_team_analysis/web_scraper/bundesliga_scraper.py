import os

import pandas as pd
import requests


def get_running_stats(url):
    """
    Retrieves running stats from a given URL and returns a DataFrame.

    Args:
        url (str): The URL to scrape the running stats from.

    Returns:
        pandas.DataFrame: The running stats as a DataFrame.
    """
    df = pd.read_html(
        url, header=0
    )  # header=0 means the first row will be used as column names
    df = df[0]  # read_html returns a list of DataFrames, we want the first one
    df.columns = [" ".join(col).strip() for col in df.columns]
    df = df.reset_index(drop=True)
    return df


def fetch_running_data_to_csv(url, year):
    """
    Fetches data from a given URL and saves it to CSV files.

    Args:
        url (str): The URL to fetch the data from.
        year (int): The year associated with the data.

    Returns:
        None
    """

    df_data = get_running_stats(url)

    # Create a directory to store the data
    directory = f"data/raw_data/{year}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, "Laufleistung.csv")
    try:
        df_data.to_csv(file_path, index=False)
        print(f"DataFrame Laufleistung saved as {file_path}")
    except Exception as e:
        print(f"Error Saving DataFrame Laufleistung could not be saved as {file_path}")
