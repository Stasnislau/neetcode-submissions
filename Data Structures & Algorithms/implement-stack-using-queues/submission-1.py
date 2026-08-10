from collections import deque
class MyStack:

    def __init__(self):
        self.first = deque()
        self.second = deque()

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        self.second.clear()
        if len(self.first) == 0:
            return -1
        while len(self.first) > 1:
            self.second.append(self.first.popleft())
        val = self.first.popleft()
        self.first = self.second.copy()
        self.second.clear()
        return val

    def top(self) -> int:
        self.second.clear()
        while len(self.first) > 1:
            self.second.append(self.first.popleft())
        val = self.first[0]
        self.first = self.second.copy()
        self.first.append(val)
        self.second.clear()
        return val

    def empty(self) -> bool:
        return len(self.first) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()