# -*- coding: utf-8 -*-
"""
Created on Fri May 26 13:32:54 2023

@author: an.medinacolmenero
"""
import subprocess as sp
import threading as td

def run_file():
    # Code to run your Python file
    subprocess.run(['python', 'animation3D.py'])

# Create a new thread
thread = td.Thread(target=run_file)

# Start the thread
thread.start()
 
print("end process")