import threading 
import time

N = 5
forks = [threading.Semaphore(1) for _ in range(N)]

def philosopher(i):
    left, right = forks[i], forks[(i+1) % N]
    while True:
        print(f"Philosopher {i} is thinking.")
        time.sleep(1)
        print(f"Philosopher {i} is hungry.")
        with left:
            with right:
                print(f"Philosopher {i} is eating.")
                time.sleep(1)

for i in range(N):
    threading.Thread(target=philosopher,args=(i,),daemon=True).start()

time.sleep(10)  # Let philosophers dine for a while
