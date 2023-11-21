def sort_dataframe_by_column(dataframe, column_name):
    """
    Diese Funktion nimmt einen DataFrame und den Namen einer Spalte,
    ordnet den DataFrame nach dieser Spalte und gibt den aktualisierten DataFrame zurück.
    """
    if column_name in dataframe.columns:
        sorted_dataframe = dataframe.sort_values(by=column_name, ascending=True)
        return sorted_dataframe
    else:
        print(f"Die Spalte {column_name} wurde nicht im DataFrame gefunden.")
        return None
    

