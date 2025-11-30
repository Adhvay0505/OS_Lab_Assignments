import os
import time

def task1_process_creation(num_children=3):
    print("\n--- Task 1: Process Creation Utility ---", flush=True)
    children = []
    for i in range(num_children):
        pid = os.fork()
        if pid == 0:
            print(f"Child {i+1}: PID={os.getpid()}, PPID={os.getppid()}, Msg=Hello from child process.", flush=True)
            os._exit(0)
        else:
            children.append(pid)
    for _ in range(num_children):
        os.wait()
    print(f"Parent PID={os.getpid()}: All children have finished.\n", flush=True)

def task2_exec_command(commands=["ls", "date", "ps"]):
    print("--- Task 2: Command Execution Using exec() ---", flush=True)
    for idx, cmd in enumerate(commands):
        pid = os.fork()
        if pid == 0:
            # Print message and flush before execvp replaces the process image
            print(f"Child {idx+1} PID={os.getpid()} executing: {cmd}", flush=True)
            os.execvp(cmd, [cmd])
            # If execvp fails:
            print(f"Exec failed in child {idx+1}", flush=True)
            os._exit(1)
        else:
            os.wait()
    print("Finished executing commands in child processes.\n", flush=True)

def run_in_subprocess(func):
    # Use fork to run a function in its own subprocess, allowing parent to continue main script
    pid = os.fork()
    if pid == 0:
        func()
        os._exit(0)
    else:
        os.wait()

def task3_zombie():
    print("--- Task 3a: Zombie Process Demonstration ---", flush=True)
    pid = os.fork()
    if pid == 0:
        print(f"Zombie Child: PID={os.getpid()} (about to exit)", flush=True)
        os._exit(0)
    else:
        print(f"Parent PID={os.getpid()} (not waiting for child PID={pid} -- child will be zombie)", flush=True)
        time.sleep(5)
        print("(Check zombie by running: ps -el | grep defunct)\n", flush=True)
        os.wait()

def task3_orphan():
    print("--- Task 3b: Orphan Process Demonstration ---", flush=True)
    pid = os.fork()
    if pid == 0:
        print(f"Orphan Child: PID={os.getpid()} sleeping, parent will exit.", flush=True)
        time.sleep(5)
        print(f"Orphan Child: PID={os.getpid()} finished (parent exited, now adopted by init).", flush=True)
        os._exit(0)
    else:
        print(f"Parent PID={os.getpid()} exiting before child PID={pid} finishes.", flush=True)
        # Instead of os._exit, just return to allow main program to continue
        return

def task4_proc_inspection(pid=None):
    print("--- Task 4: Process Info from /proc ---", flush=True)
    if pid is None:
        pid = os.getpid()
    try:
        with open(f"/proc/{pid}/status") as f:
            status_lines = f.readlines()
        exe_path = os.readlink(f"/proc/{pid}/exe")
        open_fds = os.listdir(f"/proc/{pid}/fd")
        name = next((l for l in status_lines if l.startswith("Name:")), "").strip()
        state = next((l for l in status_lines if l.startswith("State:")), "").strip()
        mem = next((l for l in status_lines if l.startswith("VmSize:")), "").strip()
        print(f"Process Info for PID {pid}:", flush=True)
        print(f"  {name}\n  {state}\n  {mem}", flush=True)
        print(f"  Executable Path: {exe_path}", flush=True)
        print(f"  Open File Descriptors: {open_fds}\n", flush=True)
    except Exception as e:
        print(f"Error reading /proc info for PID={pid}: {e}\n", flush=True)

def cpu_work(duration=2):
    # Simple CPU-bound work
    end = time.time() + duration
    while time.time() < end:
        pass

def task5_priority_demo():
    print("--- Task 5: Process Prioritization (nice values) ---", flush=True)
    nice_values = [0, 5, 10]
    for idx, nv in enumerate(nice_values):
        pid = os.fork()
        if pid == 0:
            os.nice(nv)
            print(f"Child {idx+1}: PID={os.getpid()} Nice={nv} starting CPU-bound work.", flush=True)
            cpu_work()
            print(f"Child {idx+1}: PID={os.getpid()} Nice={nv} finished CPU-bound work.", flush=True)
            os._exit(0)
    for _ in range(len(nice_values)):
        os.wait()
    print("Priority demo finished.\n", flush=True)

def print_header():
    print("\nLab Experiment Sheet-1", flush=True)
    print("School of Engineering and Technology", flush=True)
    print("Course Code & Name: ENCS351 Operating System", flush=True)
    print("Name: Adhvay Banerjee", flush=True)
    print("Roll Number: 2301410002", flush=True)
    print("Date/Time: {}".format(time.strftime("%A %d %B %Y %I:%M:%S %p %Z")), flush=True)

if __name__ == "__main__":
    print_header()
    task1_process_creation()
    task2_exec_command()
    run_in_subprocess(task3_zombie)
    run_in_subprocess(task3_orphan)
    time.sleep(6)  # Wait for orphan child to finish
    task4_proc_inspection()
    task5_priority_demo()

