# task2_system_startup_logging.py
# Simulate system boot with multiprocessing and logging

import multiprocessing
import logging
import time
import os

# Configure logging
logging.basicConfig(
    filename='system_log.txt',
    level=logging.INFO,
    format='%(asctime)s - PID:%(process)d - %(processName)s - %(message)s'
)

def process_task(name, duration=2):
    logging.info(f"{name} started")
    print(f"{name} (PID: {os.getpid()}) is running...")
    time.sleep(duration)
    logging.info(f"{name} terminated normally")
    print(f"{name} finished.")

if __name__ == '__main__':
    print("System Booting... Initializing processes...\n")
    
    processes = []
    for i in range(1, 5):
        p = multiprocessing.Process(target=process_task, args=(f"Service-Process-{i}",))
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    print("\nAll services terminated. System Shutdown Complete.")
