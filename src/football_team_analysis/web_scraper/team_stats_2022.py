import pandas as pd
import requests
import os


url_team_stats_23 = 'https://fbref.com/en/comps/20/2022-2023/2022-2023-Bundesliga-Stats'

# Define a function to get the data from the web 
def get_team_regular_season_stats(url):
    response = requests.get(url).text.replace('<!--', '').replace('-->', '')
    df = pd.read_html(response)[0]
    return df

def get_team_standard_stats(url):
    response = requests.get(url).text.replace('<!--', '').replace('-->', '')
    df = pd.read_html(response, header=1)[2]
    return df

def get_team_passing_stats(url):
    response = requests.get(url).text.replace('<!--', '').replace('-->', '')
    df = pd.read_html(response, header=1)[10]
    return df

def get_team_pass_types_stats(url):
    response = requests.get(url).text.replace('<!--', '').replace('-->', '')
    df = pd.read_html(response, header=1)[12]
    return df

def get_team_goal_shot_creation_stats(url):
    response = requests.get(url).text.replace('<!--', '').replace('-->', '')
    df = pd.read_html(response, header=1)[14]
    return df

def get_team_defensive_actions_stats(url):
    response = requests.get(url).text.replace('<!--', '').replace('-->', '')
    df = pd.read_html(response, header=1)[16]
    return df
 
def get_team_possesion_stats(url):
    response = requests.get(url).text.replace('<!--', '').replace('-->', '')
    df = pd.read_html(response, header=1)[18]
    return df

def get_team_misc_stats(url):
    response = requests.get(url).text.replace('<!--', '').replace('-->', '')
    df = pd.read_html(response, header=1)[22]
    return df


#calling the functions
regular_season = get_team_regular_season_stats(url_team_stats_23)
standard = get_team_standard_stats(url_team_stats_23)
passing = get_team_passing_stats(url_team_stats_23)
pass_types = get_team_pass_types_stats(url_team_stats_23)
goal_shot_creation = get_team_goal_shot_creation_stats(url_team_stats_23)
defensive_action = get_team_defensive_actions_stats(url_team_stats_23)
possesion = get_team_possesion_stats(url_team_stats_23)
misc = get_team_misc_stats(url_team_stats_23)


# Create a directory to store the data
directory = "../../../data/raw_data/2022"
if not os.path.exists(directory):
    os.makedirs(directory)

# Define a dictionary containing the dataframes
dataframes = {
    'regular_season': regular_season,
    'standard': standard,
    'passing': passing,
    'pass_types': pass_types,
    'goal_shot_creation': goal_shot_creation,
    'defensive_action': defensive_action,
    'possesion': possesion,
    'misc': misc
}

# Save the Data to a CSV file

for name, df in dataframes.items():
    file_path = os.path.join(directory, f"{name}_2022.csv")
    try: 
        df.to_csv(file_path, index=False)
        print(f"DataFrame '{name}' saved as {file_path}")
    except Exception as e:
        print(f"Error Saving DataFrame '{name}' could not be saved as {file_path}")


    

