import threading
import time
import random
from queue import Queue

buffer = Queue(maxsize=5)

def producer():
    while True:
        iteam = random.randint(1, 100)
        buffer.put(iteam)
        print("Produced:", iteam)
        time.sleep(random.random())

def consumer():
    while True:
        iteam = buffer.get()
        print("Consumed:", iteam)
        buffer.task_done()
        time.sleep(random.random())

threading.Thread(target=producer, daemon=True).start()
threading.Thread(target=consumer, daemon=True).start()

time.sleep(10)