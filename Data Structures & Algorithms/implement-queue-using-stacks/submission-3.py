class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        self.first.append(x)
        if len(self.second) == 0:
            self.second.append(x)
        

    def pop(self) -> int:
        if self.empty():
            return -1
        if len(self.first) == 1:
            self.second.pop()
            return self.first.pop()
        return_val = self.second.pop()
        while len(self.first) > 1:
            self.second.append(self.first.pop())
        self.first.pop()
        target = self.second[-1]
        while self.second:
            self.first.append(self.second.pop())
        self.second.append(target)
        return return_val
        

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.second[-1]
        

    def empty(self) -> bool:
        return len(self.first) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()