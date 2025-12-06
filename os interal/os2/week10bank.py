def is_safe(processes, avail,max_need, alloc):
    n = len(processes)
    m = len(avail)
    finish = [False]*n
    safe_seq = []

    need = [[max_need[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    work = avail.copy()

    while len(safe_seq) < n:
        allocated = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                work = [work[j] + alloc[i][j] for j in range(m)]
                safe_seq.append(processes[i])
                finish[i] = True
                safe_seq.append(processes[i])
                allocated = True
        if not allocated:
            return False, []
    return True, safe_seq

processes = [0, 1, 2]
avail = [3, 3, 2]
max_need = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2]
]
alloc = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2]
]           
safe, seq = is_safe(processes, avail, max_need, alloc)
print("System is safe:", safe)
if safe:
    print("Safe sequence:", seq)