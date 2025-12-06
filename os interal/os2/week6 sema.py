import multiprocessing
import time

def worker(sema, worker_id):
    sema.acquire()
    print(f"worker {worker_id} is working")
    time.sleep(2)
    print (f"worker {worker_id} is done")
    sema.release()

if __name__ == "__main__":
    semaphore = multiprocessing.Semaphore(3)
    processes = [multiprocessing.Process(target=worker, args=(semaphore,i))for i in range(7)]

    for p in processes: p.start()
    for p in processes: p.join()    