from m0_1_system_variables import bosch_filepath
from m1_0_data_identification import unaccompanied_cdrx_path_list
import psutil
import sys
import subprocess
import time
import pyautogui as gui
import pyperclip as pyp
import os


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
    print('CDR.EXE is running. Killing CDR.EXE and re-starting process to make it visible')
    subprocess.run(['taskkill', '/f', '/im', 'cdr.exe'])
else:
    process = subprocess.Popen(bosch_filepath)
    time.sleep(2)

#Must truncate the filepath for use in CDR to eliminate the filename and last backslash.
for working_file in unaccompanied_cdrx_path_list:
    working_file_dir_str = str(os.path.dirname(working_file))

    gui.hotkey('ctrl', 'o')

    gui.keyDown('shift')

    # Press the Tab key six times
    for i in range(7):
        gui.press('tab')

    # Release the Shift key
        gui.keyUp('shift')   

    gui.press('Enter')

    pyp.copy(working_file_dir_str)

    gui.hotkey('ctrl', 'v')

    gui.press('Enter')

    time.sleep(1)
    for i in range(4):
        gui.press('tab')
        time.sleep(0.1)

    time.sleep(1)

    gui.press('space')

    gui.press('enter')

    time.sleep(1)

    gui.press('alt')
    gui.press('right')

    for i in range(9):
        gui.press('down')
        time.sleep(0.1)

    for i in range(2):
        gui.press('enter')
        time.sleep(0.1)