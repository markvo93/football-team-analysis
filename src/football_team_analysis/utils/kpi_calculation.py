from football_team_analysis.utils import load_data

data_2022 = load_data.load_data("data/preprocessed_data/2022")
data_2023 = load_data.load_data("data/preprocessed_data/2023")


def tackles_won_in_percent(dataframe, season):
    tackles_won_in_percent = dataframe[["Squad", "Tkl", "TklW"]].copy()
    tackles_won_in_percent["TklW%"] = (
        tackles_won_in_percent["TklW"] / tackles_won_in_percent["Tkl"]
    ) * 100
    # save the new data frame to a csv file
    tackles_won_in_percent.to_csv(
        f"data/preprocessed_data/{season}/tackles_won_in_percent.csv", index=False
    )
    return tackles_won_in_percent


df = tackles_won_in_percent(data_2022[4], 2022)
df = tackles_won_in_percent(data_2023[4], 2023)
