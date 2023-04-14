import os
from m0_1_system_variables import raw_data_path, cdrx_path_list, unaccompanied_cdrx_path_list


#This block of code creates a list of paths to cdrx files which do not have an accompanying .CSV file. 
#The objective of this module is to find all of these 'unaccompanied' files and then create a .CSV version suitable for import and analysis. 

#Whenever the database is re-scanned for new files, the unaccompanied_cdrx_path_list must be cleared. Otherwise, it will simply add the new list of unaccompanied files to an old list.
unaccompanied_cdrx_path_list = []


for root, dirs, files in os.walk(raw_data_path):
        for filename in files:
                if filename.lower().endswith('cdrx'):
                        csv_filename = os.path.splitext(filename)[0] + '.CSV'
                        if csv_filename not in files:     
                        # os.path.join is performed to handle the case of one vehicle having multiple records. 
                        # The record is saved as the vehicle's VIN, but successive records bearing the same name are placed in different directories.  
                        # Considering the filepath as part of the record's 'identity' will ensure that these edge cases are accommodated.

                            unaccompanied_cdrx_path_list.append(os.path.join(root, filename))

                            