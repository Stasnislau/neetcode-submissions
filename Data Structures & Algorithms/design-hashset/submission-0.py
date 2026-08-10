class Node:
    def __init__(self, val = None, next = None):
        self.next = next
        self.val = val
SIZE = 10000
class MyHashSet:

    def __init__(self):
        self.arr = [Node() for _ in range(SIZE)]

    def add(self, key: int) -> None:
        index = key % SIZE
        prev = self.arr[index]
        curr = self.arr[index].next
        while curr:
            if curr.val == key:
                return
            prev = curr
            curr = curr.next
        prev.next = Node(key)
        
        

    def remove(self, key: int) -> None:
        index = key % SIZE
        curr = self.arr[index].next
        prev = self.arr[index]
        while curr:
            if curr.val == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        index = key % SIZE
        curr = self.arr[index]
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)