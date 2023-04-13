import pyautogui

import psutil

import subprocess

from m0_1_system_variables import bosch_filepath

def check_process(process_name):
    """Check if a process is running on Windows"""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

# Check if 'cdr.exe' is running
if check_process('CDR.EXE'):
    print('CDR.EXE is running.')
else:
    subprocess.Popen(['"' + bosch_filepath + '"'])
    

