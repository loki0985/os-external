class ContiguousAlloccation:
    def __init__(self, size):
        self.disk = [0] * size

    def allocate(self, start, lenght):
        if all(self.disk[i] == 0 for i in range(start, start + lenght)):
            for i in range(start, start + lenght):
                self.disk[i] = 1
            print(f"file allocated from {start} to {start + lenght - 1}")
        else:
            print("not enough space")

fs = ContiguousAlloccation(100)
fs.allocate(10, 20)
fs.allocate(15, 10)    