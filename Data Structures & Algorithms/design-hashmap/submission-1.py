class Node:
    def __init__(self, key = None,val = None, next = None):
        self.next = next
        self.val = val
        self.key = key

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.arr = [Node() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        prev = self.arr[index]
        curr = self.arr[index].next
        while curr:
            if curr.key == key:
                curr.val = value
                return
            prev = curr
            curr = curr.next
        prev.next = Node(key, value)
        

    def get(self, key: int) -> int:
        index = key % self.size
        curr = self.arr[index].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        prev = self.arr[index]
        curr = self.arr[index].next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)