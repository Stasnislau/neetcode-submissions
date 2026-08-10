class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.current_count = 0
        self.head = 0
        self.tail = 0
        self.arr = [-1] * self.k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.current_count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.current_count -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.head ) % self.k]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.tail - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.current_count == 0
        

    def isFull(self) -> bool:
        return self.current_count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()