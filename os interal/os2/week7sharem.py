from multiprocessing import Process, Value 

def add_one(shared_num):
    for _ in range(400):
        with shared_num.get_lock():
            shared_num.value += 1

if __name__ == "__main__":
    num = Value('i', 0)  # 'i' indicates a signed integer
    p1 =Process(target=add_one, args=(num,))
    p2 =Process(target=add_one, args=(num,))

    p1.start(); p2.start()
    p1.join(); p2.join()

    print("final shared value:", num.value)