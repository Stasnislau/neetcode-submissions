"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict, deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        checked = defaultdict()
        visited = set()
        def bfs(node):
            q = deque([node])
            while q:
                item = q.popleft()
                visited.add(item)
                if item not in checked:
                    checked[item] = Node(item.val)
                for nei in item.neighbors: 
                    if nei not in checked:
                        checked[nei] = Node(nei.val)
                    checked[item].neighbors.append(checked[nei])
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
                        
        bfs(node)
        return checked[node]

                    
                
            

            