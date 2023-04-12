import os
from m0_1_system_variables import raw_data_path, scanned_file_list, file_staging_list

for filename in os.listdir(raw_data_path):
    if filename.endswith('.cdrx'):
        if filename not in scanned_file_list:
            file_staging_list.append(filename)
            print(f'New file detected: {filename}')