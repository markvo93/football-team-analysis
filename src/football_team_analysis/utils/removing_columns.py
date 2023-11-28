import glob
import os

import pandas as pd


def removing_columns(path, unnecessary_columns, directory):
    # import all csv files from the folder 'data'
    all_files = glob.glob(path + "/*.csv")
    unnecessary_columns = unnecessary_columns

    # Erstelle den Zielordner, wenn er nicht existiert
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Target folder was created.")

    # Iteriere über jede Datei
    for file in all_files:
        # Lade die CSV-Datei in ein DataFrame
        data = pd.read_csv(file)

        for unnecessary_column in unnecessary_columns:
            # Lösche die gewünschte Spalte
            if unnecessary_column in data.columns:
                data = data.drop(unnecessary_column, axis=1)
                print(
                    f"Column {unnecessary_column} in {file.split('/')[-1]} has been deleted."
                )
            else:
                pass

        # Speichere das bearbeitete DataFrame in einer neuen CSV-Datei im Zielordner
        new_data_name = os.path.join(directory, f'preprocessed_{file.split("/")[-1]}')
        data.to_csv(new_data_name, index=False)
        print(f"File {file.split('/')[-1]} has been processed and saved.")
    print("All files have been processed.")

    return None
