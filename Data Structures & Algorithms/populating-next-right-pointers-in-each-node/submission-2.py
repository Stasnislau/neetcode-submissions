"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root])
        if not root:
            return None
        while q:
            size = len(q)
            for i in range(size):
                item = q.popleft()
                if i == size - 1:
                    item.next = None
                else:
                    item.next = q[0]
                if item.left:
                    q.append(item.left)
                    q.append(item.right)
        return root