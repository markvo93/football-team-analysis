import pandas as pd
import glob
import os

def removing_hash_column(path, unnecessary_column, directory):
    # import all csv files from the folder 'data'
    all_files = glob.glob(path + '/*.csv')

    # Erstelle den Zielordner, wenn er nicht existiert
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Target folder was created.")

    # Iteriere über jede Datei
    for file in all_files:
        # Lade die CSV-Datei in ein DataFrame
        data = pd.read_csv(file)

        # Lösche die gewünschte Spalte
        if unnecessary_column in data.columns:
            data = data.drop(unnecessary_column, axis=1)
            print(f"Column {unnecessary_column} in {file.split('/')[-1]} has been deleted.")
        else:
            print(f"Column {unnecessary_column} in {file.split('/')[-1]} was not found.")
            continue


        # Speichere das bearbeitete DataFrame in einer neuen CSV-Datei im Zielordner
        neuer_datei_name = os.path.join(directory, f'preprocessed_{file.split("/")[-1]}')
        data.to_csv(neuer_datei_name, index=False)
        print(f"File {file.split('/')[-1]} has been processed and saved.") 


def removing_needless_columns(path, directory):
    # import one csv file from the folder 'data'
    rs_file = glob.glob(path + '/regular_season_*.csv')
    columns = ['Attendance', 'Top Team Scorer', 'Goalkeeper', 'Notes']

    # Erstelle den Zielordner, wenn er nicht existiert
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Target folder was created.")

    
    # Iteriere über jede Datei
    for file in rs_file: 
        data = pd.read_csv(file)

        for column in columns:
            if column in data.columns:
                data = data.drop(columns, axis=1)
                print(f"Column {column} in {file.split('/')[-1]} has been deleted.")

            else:
                print(f"Column {column} in {file.split('/')[-1]} was not found.")
                continue

                

        # Speichere das bearbeitete DataFrame in einer neuen CSV-Datei im Zielordner
        neuer_datei_name = os.path.join(directory, f'preprocessed_{file.split("/")[-1]}')
        data.to_csv(neuer_datei_name, index=False)
        print(f"File {file.split('/')[-1]} has been processed and saved.")

if __name__ == "__main__":
    path = r'../../../data/raw_data/2022'
    unnecessary_column = '# Pl'
    directory = '../../../data/preprocessed_data/2022'
    removing_hash_column(path, unnecessary_column, directory)

    path = r'../../../data/raw_data/2023'
    unnecessary_column = '# Pl'
    directory = '../../../data/preprocessed_data/2023'
    removing_hash_column(path, unnecessary_column, directory)

    path = r'../../../data/raw_data/2022'
    directory = '../../../data/preprocessed_data/2022'
    removing_needless_columns(path, directory)

    path = r'../../../data/raw_data/2023'
    directory = '../../../data/preprocessed_data/2023'
    removing_needless_columns(path, directory)
