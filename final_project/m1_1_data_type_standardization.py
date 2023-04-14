import psutil
import sys
import subprocess
import pandas as pd
from m0_1_system_variables import bosch_filepath

'''This block is used to determine whether the Bosch CDR tool is running'''

def check_process(process_name):
    """Check if a process is running on Windows"""
    for proc in psutil.process_iter(['name']):
        if proc.name() == process_name:
            return True
    return False
    sys.exit(1)

# Check if 'cdr.exe' is running
if check_process('CDR.EXE'):
    print('CDR.EXE is running.')
else:
    process = subprocess.Popen(bosch_filepath)

'''This block is used to create a pandas dataframe from the csv file containing all not-yet-interpreted .CDRx files'''
with open ('unaccompanied_cdrx_path_list.csv', 'r') as path_list:
    complete_records_dataframe = pd.read_csv(path_list)



