class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n != len(edges) + 1:
            return []
        if n == 1:
            return [0]
        degree = [0] * n
        adj = defaultdict(list)
        for edg in edges:
            adj[edg[0]].append(edg[1])
            adj[edg[1]].append(edg[0])
            degree[edg[0]] += 1
            degree[edg[1]] += 1
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        while n > 2:
            size = len(q)
            for _ in range(size):
                item = q.popleft()
                for child in adj[item]:
                    degree[child] -= 1
                    if degree[child] == 1:
                        q.append(child)
            n -= size
        return list(q)
