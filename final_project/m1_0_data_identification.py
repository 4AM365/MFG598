import os
# from m0_1_system_variables import raw_data_path, scanned_file_list, file_staging_list
from m0_1_system_variables import scanned_file_list, file_staging_list

raw_data_path = r'H:\LOSS1\EDR\Downloaded Files'

for root, dirs, files in os.walk(raw_data_path):
    for filename in files:
        if filename.endswith('.cdrx'):
            # Check for the presence of a .csv file with the same name
            csv_filename = os.path.splitext(filename)[0] + ".csv"
            csv_filepath = os.path.join(root, csv_filename)

            if os.path.exists(csv_filepath) and filename not in scanned_file_list:
                file_staging_list.append(filename)
                print(f'New file detected: {os.path.join(root, filename)}')

print(file_staging_list) 