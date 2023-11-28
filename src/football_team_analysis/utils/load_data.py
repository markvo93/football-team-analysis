import glob

import pandas as pd


def load_data(path):
    # Load all CSV files in the specified folder
    all_files = glob.glob(path + "/*.csv")

    # Check if files were found
    if not all_files:
        print("No CSV files found in the specified folder.")
        return

    # Create an empty list to store the dataframes
    dfs = []

    # Iterate through CSV files and load each into a separate DataFrame
    for file in all_files:
        df = pd.read_csv(file)
        dfs.append(df)  # Append each DataFrame to the list

    # Return the list of dataframes
    return dfs


print(load_data("data/preprocessed_data/2022"))
