def sort_dataframe_by_column(dataframe, column_name):
    """
    This function takes a DataFrame and the name of a column,
    arranges the DataFrame ascending according to this column and returns the updated DataFrame.
    """
    if column_name in dataframe.columns:
        sorted_dataframe = dataframe.sort_values(by=column_name, ascending=False)
        return sorted_dataframe
    else:
        print(f"Column {column_name} hasn't been found in the dataframe.")
        return None
    

