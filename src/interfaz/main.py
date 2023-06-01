# -*- coding: utf-8 -*-
"""
Created on Fri May 26 13:32:54 2023

@author: an.medinacolmenero
"""


import subprocess
import threading as td

import threading

def run_file():
    # Code to run your Python file
    subprocess.run(['python', 'buttons_Vpython.py'])

# Create a new thread
thread = threading.Thread(target=run_file)

# Start the thread
thread.start()

# Main thread continues executing other code

# Wait for the thread to complete (optional)
#thread.join()


print("end process")