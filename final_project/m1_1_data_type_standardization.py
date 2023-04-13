import pyautogui

import psutil

import sys

from m0_1_system_variables import bosch_filepath

'''
This section of code checks if the program is open.
'''

def check_process(process_name):
    """Check if a process is running on Windows"""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False
    sys.exit(1)

# Check if 'cdr.exe' is running
if check_process('CDR.EXE'):
    print('CDR.EXE is running.')
else:
    print(f'Open CDR.EXE from {bosch_filepath}')


