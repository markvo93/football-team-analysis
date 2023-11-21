import pandas as pd 

# urls for scraping
url_player_stats_22 = "https://fbref.com/en/comps/Big5/2022-2023/stats/players/2022-2023-Big-5-European-Leagues-Stats"
url_player_stats_23 = "https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats"


def get_player_stats_22(url):
    df = pd.read_html(url)
    df = df[0]
    df.columns = [' '.join(col).strip() for col in df.columns]
    df = df.reset_index(drop=True)
    return df

def get_player_stats_23(url):
    df = pd.read_html(url)
    df = df[0]
    df.columns = [' '.join(col).strip() for col in df.columns]
    df = df.reset_index(drop=True)
    return df

def get_team_stats_22(url):
    df = pd.read_html(url)
    df = df[0]
    df.columns = [' '.join(col).strip() for col in df.columns]
    df = df.reset_index(drop=True)
    return df

 
# call the functions
player_stats_22 = get_player_stats_22(url_player_stats_22)
player_stats_23 = get_player_stats_23(url_player_stats_23)

# save the dataframes into raw_data folder
player_stats_22.to_csv("../../data/raw_data/player_stats_2022.csv")
player_stats_23.to_csv("../../data/raw_data/player_stats_2023.csv")
