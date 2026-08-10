class Tree:
    

    def __init__(self, start = 0, end = 0):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, node, start, end):
        if not node:
            return False
        if start >= node.end:
            if not node.right:
                node.right = Tree(start, end)
                return True
            return self.insert(node.right, start, end)
        elif end <= node.start:
            if not node.left:
                node.left = Tree(start, end)
                return True
            return self.insert(node.left, start, end)
        else:
            return False

class MyCalendar:
    def __init__(self):
        self.root = Tree()

    def book(self, startTime: int, endTime: int) -> bool:
        return self.root.insert(self.root, startTime, endTime)


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)