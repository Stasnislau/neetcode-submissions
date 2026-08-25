class RandomizedSet:

    def __init__(self):
        self.size = 0
        self.indexes = {}
        self.store = []


    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        self.indexes[val] = self.size
        self.size += 1
        self.store.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False
        index = self.indexes[val]
        self.indexes[self.store[-1]] = index
        self.store[index], self.store[-1] = self.store[-1], self.store[index]
        self.store.pop()
        self.indexes.pop(val)
        self.size -= 1
        return True

    def getRandom(self) -> int:
        if self.size == 0:
            return None
        index = random.randrange(self.size)
        return self.store[index]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()