import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# Input
processes = ['P1','P2','P3','P4']
burst_time = [10, 5, 8, 6]
arrival_time = [0, 1, 2, 3]
time_quantum = 4  # For Round Robin

# --------------------------
# 1. FCFS Scheduling
def fcfs(processes, burst_time, arrival_time):
    n = len(processes)
    start_time = [0]*n
    completion_time = [0]*n
    waiting_time = [0]*n
    turnaround_time = [0]*n

    start_time[0] = arrival_time[0]
    completion_time[0] = start_time[0] + burst_time[0]
    turnaround_time[0] = completion_time[0] - arrival_time[0]
    waiting_time[0] = turnaround_time[0] - burst_time[0]

    for i in range(1, n):
        start_time[i] = max(completion_time[i-1], arrival_time[i])
        completion_time[i] = start_time[i] + burst_time[i]
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    gantt = [(processes[i], start_time[i], completion_time[i]) for i in range(n)]

    df = pd.DataFrame({
        'Process': processes,
        'Arrival': arrival_time,
        'Burst': burst_time,
        'Start': start_time,
        'Completion': completion_time,
        'Waiting': waiting_time,
        'Turnaround': turnaround_time
    })

    avg_wt = sum(waiting_time)/n
    avg_tat = sum(turnaround_time)/n

    return df, gantt, avg_wt, avg_tat

# --------------------------
# 2. SJF (Non-preemptive)
def sjf(processes, burst_time, arrival_time):
    n = len(processes)
    remaining = list(range(n))
    time = 0

    start_time = [0]*n
    completion_time = [0]*n
    waiting_time = [0]*n
    turnaround_time = [0]*n

    while remaining:
        arrived = [i for i in remaining if arrival_time[i] <= time]

        if not arrived:
            time += 1
            continue

        idx = min(arrived, key=lambda x: burst_time[x])
        start_time[idx] = time
        time += burst_time[idx]
        completion_time[idx] = time

        turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]

        remaining.remove(idx)

    gantt = sorted(
        [(processes[i], start_time[i], completion_time[i]) for i in range(n)],
        key=lambda x: x[1]
    )

    df = pd.DataFrame({
        'Process': processes,
        'Arrival': arrival_time,
        'Burst': burst_time,
        'Start': start_time,
        'Completion': completion_time,
        'Waiting': waiting_time,
        'Turnaround': turnaround_time
    })

    avg_wt = sum(waiting_time)/n
    avg_tat = sum(turnaround_time)/n

    return df, gantt, avg_wt, avg_tat

# --------------------------
# 3. Round Robin Scheduling (Corrected)
def round_robin(processes, burst_time, arrival_time, tq):
    n = len(processes)
    rem_bt = burst_time.copy()
    t = 0

    gantt = []
    waiting_time = [0]*n
    turnaround_time = [0]*n
    completion_time = [0]*n

    ready_queue = []
    visited = [False]*n
    completed = 0

    # Add processes with arrival time 0
    for i in range(n):
        if arrival_time[i] == 0:
            ready_queue.append(i)
            visited[i] = True

    while completed < n:
        if not ready_queue:
            t += 1
            for i in range(n):
                if arrival_time[i] <= t and not visited[i]:
                    ready_queue.append(i)
                    visited[i] = True
            continue

        i = ready_queue.pop(0)
        start = t

        if rem_bt[i] > tq:
            t += tq
            rem_bt[i] -= tq
            gantt.append((processes[i], start, t))
        else:
            t += rem_bt[i]
            gantt.append((processes[i], start, t))
            rem_bt[i] = 0
            completed += 1
            completion_time[i] = t

        # Add newly arrived processes
        for j in range(n):
            if arrival_time[j] <= t and not visited[j]:
                ready_queue.append(j)
                visited[j] = True

        # Re-add unfinished process
        if rem_bt[i] > 0:
            ready_queue.append(i)

    for i in range(n):
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    df = pd.DataFrame({
        'Process': processes,
        'Arrival': arrival_time,
        'Burst': burst_time,
        'Completion': completion_time,
        'Waiting': waiting_time,
        'Turnaround': turnaround_time
    })

    avg_wt = sum(waiting_time)/n
    avg_tat = sum(turnaround_time)/n

    return df, gantt, avg_wt, avg_tat

# --------------------------
# Gantt Chart Plot Function
def plot_gantt(gantt, title):
    fig, ax = plt.subplots(figsize=(10,2))
    for p, start, end in gantt:
        ax.barh(1, end-start, left=start, edgecolor='black')
        ax.text((start+end)/2, 1, p, ha='center', va='center')

    ax.set_xlim(0, max([end for _,_,end in gantt])+2)
    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title(title)
    plt.show()

# --------------------------
# Run Algorithms
fcfs_table, fcfs_gantt, fcfs_wt, fcfs_tat = fcfs(processes, burst_time, arrival_time)
sjf_table, sjf_gantt, sjf_wt, sjf_tat = sjf(processes, burst_time, arrival_time)
rr_table, rr_gantt, rr_wt, rr_tat = round_robin(processes, burst_time, arrival_time, time_quantum)

# --------------------------
# Plot Gantt Charts
plot_gantt(fcfs_gantt, "FCFS Gantt Chart")
plot_gantt(sjf_gantt, "SJF Gantt Chart")
plot_gantt(rr_gantt, "Round Robin Gantt Chart")

# --------------------------
# Print Tables
print("\n--- FCFS Table ---")
print(fcfs_table)

print("\n--- SJF Table ---")
print(sjf_table)

print("\n--- Round Robin Table ---")
print(rr_table)

# --------------------------
# Comparison Table
comparison = pd.DataFrame({
    'Algorithm': ['FCFS', 'SJF', 'Round Robin'],
    'Average Waiting Time': [fcfs_wt, sjf_wt, rr_wt],
    'Average Turnaround Time': [fcfs_tat, sjf_tat, rr_tat]
})

print("\n--- Comparison Table ---")
print(comparison)
