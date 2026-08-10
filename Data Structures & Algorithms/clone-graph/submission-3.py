"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        checked = {}
        def bfs(node):
            q = deque([node])
            if node not in checked:
                checked[node] = Node(node.val)
            while q:
                item = q.popleft()
                for nei in item.neighbors: 
                    if nei not in checked:
                        checked[nei] = Node(nei.val)
                        q.append(nei)
                    checked[item].neighbors.append(checked[nei])
                        
        bfs(node)
        return checked[node]

                    
                
            

            