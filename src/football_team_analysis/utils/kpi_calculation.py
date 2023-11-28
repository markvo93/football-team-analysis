from football_team_analysis.utils import load_data

data_2022 = load_data.load_data("data/preprocessed_data/2022")


def tackles_won_in_percent(dataframe):
    tackles_won_in_percent = dataframe[["Squad", "Tkl", "TklW"]]
    tackles_won_in_percent["TklW%"] = (
        tackles_won_in_percent["TklW"] / tackles_won_in_percent["Tkl"]
    ) * 100
    print(tackles_won_in_percent)


df = tackles_won_in_percent(data_2022[4])
print(df)
