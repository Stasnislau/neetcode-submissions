from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        g = defaultdict(list)
        for n1,n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)
        q = deque([0])
        visited = set()
        visited.add(0)
        while q:
            curr = q.popleft()
            for nei in g[curr]:
                if not nei in visited:
                    q.append(nei)
                    visited.add(nei)

        return len(visited) == n



            