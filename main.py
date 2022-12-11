import pandas as pd


def save_file_with_separate_sheets(
    source_file_name, save_file_name, target_column, target_datatype
):
    '''
    Saves an Excel file with separate sheets for each unique value
    in the specified target column.
    '''

    # Read the source file using the specified target column and datatype
    dt = pd.read_csv(
        source_file_name,
        index_col=0,
        dtype={target_column: target_datatype}
    )
    # Extract the target data from the DataFrame
    target_data = dt[target_column]

    # Get the set of unique values in the target data
    target_data_set = set()
    for data in target_data:
        if (data not in target_data_set) and (type(data) == target_datatype):
            target_data_set.add(data)

    # Create an ExcelWriter object
    with pd.ExcelWriter(f"{save_file_name}.xlsx") as writer:
        # Iterate over the unique values in the target data and
        # Write each value to a separate sheet in the Excel file
        for data in target_data_set:
            dt[target_data == data].to_excel(writer, sheet_name=data)


# Example usage:
save_file_with_separate_sheets(
    '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv',
    'test',
    'Primary Fur Color',
    str
)
