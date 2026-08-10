class Node:
    def __init__(self, val: int, key: int | None = None, prev: Node | None = None, next: Node | None = None, ):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.freeSpace = capacity
        self.head = Node(-1)
        self.tail = Node(-1, None, self.head)
        self.head.next = self.tail
        self.maps = {}

    def _moveToMostRecent(self, node: Node):
        if node.next != self.tail:
            node.next.prev = node.prev
            node.prev.next = node.next

            node.prev = self.tail.prev
            node.prev.next = node
            node.next = self.tail
            self.tail.prev = node

    def get(self, key: int) -> int:
        if self.maps.get(key):
            node = self.maps.get(key)
            self._moveToMostRecent(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.maps.get(key):
            node = self.maps.get(key)
            self._moveToMostRecent(node)
            if node.val != value:
                node.val = value
        else:
            node = Node(value, key)
            if self.freeSpace == 0:
                self.freeSpace += 1
                nodeToBeDeleted = self.head.next
                print(nodeToBeDeleted.val,nodeToBeDeleted.key, 'deleted' )
                self.head.next = nodeToBeDeleted.next
                nodeToBeDeleted.next.prev = self.head
                nodeToBeDeleted.next = None
                nodeToBeDeleted.prev = None
                self.maps.pop(nodeToBeDeleted.key)
    
            self.freeSpace -= 1
            node.prev = self.tail.prev
            node.prev.next = node
            node.next = self.tail
            self.tail.prev = node
            self.maps[key] = node
            print(node.val, self.freeSpace)
            current = self.head
            while current:
                print(current.val, 'lists')
                current = current.next





        

        
