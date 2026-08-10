class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        matrix = [([0] * k) for _ in range(1,k + 1)]
        row_adj = {i: set() for i in range(1,k+1)}
        row_indegree = {i: 0 for i in range(1,k + 1)}
        for in_rule, out_rule in rowConditions:
            if out_rule not in row_adj[in_rule]:
                row_indegree[out_rule] += 1
            row_adj[in_rule].add(out_rule)
        col_adj = {i: set() for i in range(1,k+1)}
        col_indegree = {i: 0 for i in range(1,k + 1)}
        for in_rule, out_rule in colConditions:
            if out_rule not in col_adj[in_rule]:
                col_indegree[out_rule] += 1
            col_adj[in_rule].add(out_rule)
        def get_order(indegree, adj):
            q = deque()
            visited = set()
            res = []
            for key, deg in indegree.items():
                if deg == 0:
                    q.append(key)
                    visited.add(key)
                    res.append(key)
            while q:
                item = q.popleft()
                for child in adj[item]:
                    if child not in visited:
                        indegree[child] -= 1
                        if indegree[child] == 0:
                            q.append(child)
                            visited.add(child)
                            res.append(child)
            return res
        col_order = get_order(col_indegree, col_adj)
        row_order = get_order(row_indegree, row_adj)
        if len(col_order) != k or len(row_order) != k:
            return []
        row_of = {}
        col_of = {}
        for i in range(len(col_order)):
            row_of[row_order[i]] = i
            col_of[col_order[i]] = i
        for i in range(1, len(col_order) + 1):
            y = row_of[i]
            x = col_of[i]
            matrix[y][x] = i

        return matrix


