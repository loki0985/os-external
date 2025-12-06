class IndexedAllocation:
    def __init__(self , size):
        self.disk = [0] * size

    def allocate(self, index_block, blocks):    
        if self .disk[index_block] == 0 and all(self.disk[b] == 0 for b in blocks):
            self.disk[index_block] = blocks
            for b in blocks:
                self.disk[b] = 1  # Mark block as used
            print(f"file allocated with index block {index_block} and data blocks {blocks}")
        else:
            print("error : block already in use")

fs = IndexedAllocation(50)
fs.allocate(2, [5, 10, 15,35])
