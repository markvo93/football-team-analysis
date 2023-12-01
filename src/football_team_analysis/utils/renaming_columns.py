import pandas as pd

df1 = pd.read_csv("data/raw_data/2023/Laufleistung.csv")
df2 = pd.read_csv("data/raw_data/2022/Laufleistung.csv")


def rename_columns(dataframe, new_names):
    dataframe.columns = new_names
    return dataframe


def drop_columns(dataframe, columns_to_drop):
    dataframe = dataframe.drop(columns=columns_to_drop)
    return dataframe


for df, year in [(df1, 2023), (df2, 2022)]:
    df = rename_columns(df, ["#", "Unnamed:1", "Squad", "Games", "Km", "km/perG"])
    df = drop_columns(df, ["#", "Unnamed:1"])
    df.to_csv(f"data/preprocessed_data/{year}/Laufleistung.csv")
