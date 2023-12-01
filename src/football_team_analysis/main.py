import football_team_analysis
from football_team_analysis.utils.removing_columns import removing_columns
from football_team_analysis.web_scraper.bundesliga_scraper import (
    fetch_running_data_to_csv,
    get_running_stats,
)
from football_team_analysis.web_scraper.team_stats import fetch_data_to_csv


def main():
    url_team_stats_22_23 = (
        "https://fbref.com/en/comps/20/2022-2023/2022-2023-Bundesliga-Stats"
    )

    url_team_stats_23_24 = "https://fbref.com/en/comps/20/Bundesliga-Stats"

    url_running_stats_22_23 = "https://www.sport.de/fussball/deutschland-bundesliga/se45495/2022-2023/teamstatistik-laufleistung/"
    url_running_stats_23_24 = "https://www.sport.de/fussball/deutschland-bundesliga/se51884/2023-2024/teamstatistik-laufleistung/"

    raw_data_paths = {
        2022: "data/raw_data/2022",
        2023: "data/raw_data/2023",
    }

    preprocessed_data_paths = {
        2022: "data/preprocessed_data/2022",
        2023: "data/preprocessed_data/2023",
    }

    unnecessary_columns = [
        "Attendance",
        "Top Team Scorer",
        "Goalkeeper",
        "Notes",
        "# Pl",
    ]

    fetch_data_to_csv(url_team_stats_22_23, 2022)
    fetch_data_to_csv(url_team_stats_23_24, 2023)
    fetch_running_data_to_csv(url_running_stats_22_23, 2022)
    fetch_running_data_to_csv(url_running_stats_23_24, 2023)

    for year in (2022, 2023):
        removing_columns(
            raw_data_paths[year], unnecessary_columns, preprocessed_data_paths[year]
        )


if __name__ == "__main__":
    main()
