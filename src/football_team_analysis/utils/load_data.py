import pandas as pd
import matplotlib.pyplot as plt
import glob

def load_data(folder_path):
    # Load all Excel files in the specified folder
    all_files = glob.glob(folder_path + "/*.csv")

    # Check if files were found
    if not all_files:
        print("No CSV files found in the specified folder.")
        return

    # List to store individual DataFrames for each Excel file
    all_dataframes = []

    # Iterate through Excel files and load each into a separate DataFrame
    for file in all_files:
        df = pd.read_csv(file)
        all_dataframes.append(df)

    # Optionally, you can perform operations or visualizations on each DataFrame here
    return all_dataframes
