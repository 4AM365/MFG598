import os
import pandas as pd
import chardet

from m0_1_system_variables import raw_data_path


complete_csv_path_list = []
for root, dirs, files in os.walk(raw_data_path):
        for filename in files:
                if filename.lower().endswith('csv'):
                    complete_csv_path_list.append(r"{0}\{1}".format(root, filename))



data_type = []
# Determine the file encoding
for file_path in complete_csv_path_list:
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    file_encoding = result['encoding']
    data_type.append(file_encoding)


# Create an empty list to store the dataframes
df_list = []
vin_list = []
# Iterate through each file path in the list
for file_path in complete_csv_path_list:
    # Read the CSV file into a dataframe
    # Difficulty here: some files are ascii and some files are 'Windows-1252' encoding.
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        detected_encoding = result['encoding']

    df = pd.read_csv(file_path, delimiter = '\r\n', encoding = detected_encoding, engine = 'python', names = ['Complete Record'])
    df_list.append(df)

master_dataframe = pd.DataFrame(columns=['Complete Records'])

for object in df_list:
    master_dataframe = pd.concat([master_dataframe, pd.DataFrame({'Complete Records': [object]})], ignore_index=True)