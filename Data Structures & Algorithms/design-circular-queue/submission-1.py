class Node:
    def __init__(self, val = None, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.current_count = 0
        self.head = Node()
        self.tail = Node(None, self.head, self.head)
        self.head.next = self.tail
        self.head.prev = self.tail

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value, self.tail.prev, self.tail )
        self.tail.prev = new_node
        new_node.prev.next = new_node
        self.current_count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        curr = self.head.next
        curr.next.prev = self.head
        self.head.next = curr.next
        self.current_count -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val
        

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