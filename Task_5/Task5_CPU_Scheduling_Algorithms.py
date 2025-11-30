# scheduling_algorithms.py
# Implements FCFS, SJF, Priority, Round Robin

def fcfs(processes):
    wt, tat = [], []
    time = 0
    for p in processes:
        wt.append(time)
        time += p[1]
        tat.append(time)
    return wt, tat

def sjf(processes):
    proc = sorted(processes, key=lambda x: x[1])
    return fcfs(proc)

def priority_scheduling(processes):
    proc = sorted(processes, key=lambda x: x[2])  # lower number = higher priority
    return fcfs(proc)

def round_robin(processes, quantum=2):
    n = len(processes)
    remaining = [p[1] for p in processes]
    wt = [0] * n
    time = 0
    
    while any(remaining):
        for i in range(n):
            if remaining[i] > 0:
                if remaining[i] > quantum:
                    time += quantum
                    remaining[i] -= quantum
                else:
                    time += remaining[i]
                    wt[i] = time - processes[i][1]
                    remaining[i] = 0
    tat = [wt[i] + processes[i][1] for i in range(n)]
    return wt, tat

# Sample processes: [PID, Burst Time, Priority (lower = higher)]
processes = [
    [1, 6, 2],
    [2, 8, 1],
    [3, 7, 3],
    [4, 3, 4]
]

print("Process Table:")
print("PID\tBT\tPriority")
for p in processes:
    print(f"{p[0]}\t{p[1]}\t{p[2]}")

print("\n1. FCFS:")
wt, tat = fcfs(processes)
print(f"Waiting Time: {wt} → Avg: {sum(wt)/len(wt):.2f}")
print(f"Turnaround Time: {tat} → Avg: {sum(tat)/len(tat):.2f}")

print("\n2. SJF (Non-Preemptive):")
wt, tat = sjf(processes)
print(f"Waiting Time: {wt} → Avg: {sum(wt)/len(wt):.2f}")

print("\n3. Priority Scheduling:")
wt, tat = priority_scheduling(processes)
print(f"Waiting Time: {wt} → Avg: {sum(wt)/len(wt):.2f}")

print("\n4. Round Robin (Quantum=2):")
wt, tat = round_robin(processes, 2)
print(f"Waiting Time: {wt} → Avg: {sum(wt)/len(wt):.2f}")
