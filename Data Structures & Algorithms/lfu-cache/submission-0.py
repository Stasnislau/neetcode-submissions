class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class Container:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.vals = {}
        self.count = 0
    
    def put(self, key, val):
        # Если ключ уже был, сначала выкинем старую ноду
        if key in self.vals:
            self._del_node(self.vals[key])
            self.count -= 1
        
        node = Node(key, val)
        self._append_node(node)
        self.vals[key] = node
        self.count += 1
    
    def pop_left(self):
        if self.count == 0: return None
        node = self.head.next
        self._del_node(node)
        self.vals.pop(node.key)
        self.count -= 1
        return node.key
    
    def get(self, key):
        if key not in self.vals: return None
        node = self.vals[key]
        # Мы НЕ удаляем из self.vals здесь, потому что мы просто 
        # вынимаем ноду из списка, чтобы переложить её в другой бакет
        self._del_node(node)
        self.vals.pop(key)
        self.count -= 1
        return node

    def _del_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def _append_node(self, node):
        # Добавляем ПЕРЕД tail (самые новые — в конце)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_num = 0
        self.keys_to_freqs = {}
        self.min_freq = 0
        self.collections = {}

    def _update_node(self, node, freq):
        # Вынимаем из старой коллекции
        self.collections[freq].get(node.key)
        
        # Если бакет с минимальной частотой опустел — двигаем min_freq
        if freq == self.min_freq and self.collections[freq].count == 0:
            self.min_freq += 1
            
        # Кладём в новую
        new_freq = freq + 1
        self.keys_to_freqs[node.key] = new_freq
        if new_freq not in self.collections:
            self.collections[new_freq] = Container()
        self.collections[new_freq].put(node.key, node.val)

    def get(self, key: int) -> int:
        if self.capacity == 0 or key not in self.keys_to_freqs:
            return -1
        
        freq = self.keys_to_freqs[key]
        node = self.collections[freq].vals[key]
        res = node.val
        self._update_node(node, freq)
        return res

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        
        if key in self.keys_to_freqs:
            freq = self.keys_to_freqs[key]
            node = self.collections[freq].vals[key]
            node.val = value # Обновляем значение!
            self._update_node(node, freq)
        else:
            if self.current_num == self.capacity:
                # EVICT!
                old_key = self.collections[self.min_freq].pop_left()
                self.keys_to_freqs.pop(old_key)
                self.current_num -= 1
            
            # Вставляем нового
            self.min_freq = 1
            self.keys_to_freqs[key] = 1
            if 1 not in self.collections:
                self.collections[1] = Container()
            self.collections[1].put(key, value)
            self.current_num += 1
