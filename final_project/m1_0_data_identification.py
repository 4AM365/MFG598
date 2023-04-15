import os
from m0_1_system_variables import raw_data_path
import pandas as pd


#This block of code creates a list of paths to cdrx files which do not have an accompanying .CSV file. 
#The objective of this module is to find all of these 'unaccompanied' files and then create a .CSV version suitable for import and analysis. 

#Whenever the database is re-scanned for new files, the unaccompanied_cdrx_path_list must be cleared. Otherwise, it will simply add the new list of unaccompanied files to an old list.

unaccompanied_cdrx_path_list = []
complete_cdrx_path_list = []

for root, dirs, files in os.walk(raw_data_path):
        for filename in files:
                if filename.lower().endswith('cdrx'):
                        complete_cdrx_path_list.append(r"{0}\{1}".format(root, filename))
                        csv_filename = os.path.splitext(filename)[0] + '.CSV'
                        if csv_filename not in files:     
                        # os.path.join is performed to handle the case of one vehicle having multiple records. 
                        # The record is saved as the vehicle's VIN, but successive records bearing the same name are placed in different directories.  
                        # Considering the filepath as part of the record's 'identity' will ensure that these edge cases are accommodated.

                                # unaccompanied_cdrx_path_list.append(os.path.join(root, filename))
                                #Updating this to raw string for 'cleanliness' and resilience. This prevents any need to escape the backslashes.
                                unaccompanied_cdrx_path_list.append(r"{0}\{1}".format(root, filename))



dfs = []

for file_path in complete_cdrx_path_list:

        df = pd.DataFrame({'filepath': [file_path]})

        # Append the DataFrame to the list of DataFrames
        dfs.append(df)
# Combine the list of DataFrames into a single DataFrame
complete_path_list_dataframe = pd.concat(dfs, ignore_index=True)