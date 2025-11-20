# task1_batch_processing.py
# Batch Processing Simulation - Executes multiple Python scripts sequentially

import subprocess
import os

# List of scripts to execute (place dummy scripts in same folder or update paths)
scripts = ['script1.py', 'script2.py', 'script3.py']

print("=== Starting Batch Processing Simulation ===\n")

for script in scripts:
    if not os.path.exists(script):
        print(f"Warning: {script} not found! Skipping...")
        continue
    
    print(f"Executing {script}...")
    try:
        result = subprocess.call(['python3', script])
        if result == 0:
            print(f"Success: {script} executed successfully.\n")
        else:
            print(f"Failed: {script} terminated with exit code {result}\n")
    except Exception as e:
        print(f"Error executing {script}: {e}\n")

print("=== Batch Processing Completed ===")
