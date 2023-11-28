import football_team_analysis
from football_team_analysis.utils.removing_columns import removing_columns
from football_team_analysis.web_scraper.team_stats_2022 import fetch_data_to_csv

url_team_stats_22_23 = (
    "https://fbref.com/en/comps/20/2022-2023/2022-2023-Bundesliga-Stats"
)
url_team_stats_23_24 = "https://fbref.com/en/comps/20/Bundesliga-Stats"

raw_data_path = "data/raw_data/2022"
preprocessed_data_path = "data/preprocessed_data/2022"

unnecessary_columns = [
    "Attendance",
    "Top Team Scorer",
    "Goalkeeper",
    "Notes",
    "# Pl",
]


if __name__ == "__main__":
    fetch_data_to_csv(url_team_stats_22_23, 2022)
    fetch_data_to_csv(url_team_stats_23_24, 2023)
    removing_columns(raw_data_path, unnecessary_columns, preprocessed_data_path)
