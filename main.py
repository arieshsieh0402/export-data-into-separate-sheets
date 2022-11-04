import pandas as pd


source_file_name = "file_name"
save_file_name = 'file_name'
target_column = 'column_name'
target_datatype = str


def save_file_with_separate_sheets(target_data):
    """
    Get the set of target column from the data.
    """

    target_data_set = set()
    for data in target_data:
        if (data not in target_data_set) and (type(data) == target_datatype):
            target_data_set.add(data)

    with pd.ExcelWriter(f"{save_file_name}.xlsx") as writer:
        for data in target_data_set:
            dt[target_data == data].to_excel(writer, sheet_name=data)


dt = pd.read_csv(
    source_file_name,
    index_col=0,
    dtype={target_column: target_datatype}
)
target_data = dt[target_column]
save_file_with_separate_sheets(target_data)
