from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        g = defaultdict(list)
        for item1, item2 in edges:
            g[item1].append(item2)
            g[item2].append(item1)
        
        visited = set()
        visited.add(0)
        q = deque([0])
        while q:
            item = q.popleft()
            for node in g[item]:
                if node not in visited:
                    q.append(node)
                    visited.add(node)

        
        return len(visited) == n
        
            