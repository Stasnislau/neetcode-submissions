class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for (num, denum), val in zip(equations, values):
            adj[num].append([denum, val])
            adj[denum].append([num, 1/val])
        def calc_query(src, dist):
            q = deque([[src,1]])
            visited = { src }
            while q:
                item = q.popleft()
                curr, val = item
                if not curr in adj or not dist in adj:
                    return -1 
                if curr == dist:
                    return val
                
                for child in adj[curr]:
                    if child[0] not in visited:
                        q.append((child[0], child[1] * val))
            return -1
        res = []
        for src, dist in queries:
            res.append(calc_query(src, dist))
        return res

                
                