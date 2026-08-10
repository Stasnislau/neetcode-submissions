class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1] * n
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x,y):
            par_x = find(x)
            par_y = find(y)
            if par_x == par_y:
                return False
            if rank[par_x] > rank[par_y]:
                rank[par_x] += rank[par_y]
                parents[par_y] = par_x
            else: 
                rank[par_y] += rank[par_x]
                parents[par_x] = par_y
            return True
        components = 0
        for n1,n2 in edges:
            if union(n1,n2):
                components += 1
        return n - components
                