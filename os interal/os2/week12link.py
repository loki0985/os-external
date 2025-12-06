class LinkedAllocation:
    def __init__(self, size):
        self.disk = [0] * size
        
    def allocate(self, blocks):
        for i in range(len(blocks) -1 ):
            for i in range(len(blocks) -1 ):
                self.disk[blocks[i]] = blocks[i+1]
        self.disk[blocks[-1]] = -1  # End of file marker
        print(f"file allocated with blocks: {blocks}")

fs = LinkedAllocation(20)
fs.allocate([5, 10, 15, 11])        
          