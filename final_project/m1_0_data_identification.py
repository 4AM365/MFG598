import os
from m0_1_system_variables import raw_data_path, scanned_file_list, file_staging_list, cdrx_path_list


file_count = 0
for root, dirs, files in os.walk(raw_data_path):
        for filename in files:
                if filename.lower().endswith('cdrx'):     
                        # os.path.join is performed to handle the case of one vehicle having multiple records. 
                        # The record is saved as the vehicle's VIN, but successive records bearing the same name are placed in different directories.  
                        # Considering the filepath as part of the record's 'identity' will ensure that these edge cases are accommodated.
                        cdrx_path_list.append(os.path.join(root, filename))

