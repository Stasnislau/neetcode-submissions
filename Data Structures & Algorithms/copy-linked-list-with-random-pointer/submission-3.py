"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        table = {}
        curr = head
        if not head:
            return None
        while curr:
            table[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                table[curr].next = table[curr.next]
            else:
                table[curr].next = None
            if curr.random:
                table[curr].random = table[curr.random]
            else:
                table[curr].random = None
            curr = curr.next

        return table[head]


        