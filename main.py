import pandas as pd


SOURCE_FILE_NAME = "your_file_name"
SAVE_FILE_NAME = 'export_file_name'
TARGET_COLUMN = 'column_name'
TARGET_DATATYPE = str


def find_target(data):
    """
    Get the set of target column from the data.
    """
    target_data_set = set()
    for i in data:
        if (i not in target_data_set) and (type(i) == TARGET_DATATYPE):
            target_data_set.add(i)
    return target_data_set


dt = pd.read_csv(SOURCE_FILE_NAME,
                 index_col=0,
                 dtype={TARGET_COLUMN: TARGET_DATATYPE}
                 )

target_data = dt[TARGET_COLUMN]

target_data_set = find_target(target_data)

print(target_data_set)


# Writing the data to each sheet in excel in sequence,
# and save it to the default path (current path)

with pd.ExcelWriter(f"{SAVE_FILE_NAME}.xlsx") as writer:
    for i in target_data_set:
        dt[target_data == i].to_excel(writer, sheet_name=i)
