#NTFS database of source files
import os

raw_data_path = r'H:\LOSS1\EDR\Downloaded Files'

bins = 10

bosch_filepath = os.path.join('C:', 'Program Files (x86)', 'Bosch', 'Crash Data Retrieval', 'CDR.EXE')

#This is the list of files that have already been imported into the system.
scanned_file_list = []

#This is a 'to-do' for files that need to be converted.
file_staging_list = []

complete_file_list = []

complete_path_list = []

cdrx_path_list = []

unaccompanied_cdrx_path_list = []