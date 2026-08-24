class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [1] * (n + 1)
        parents = [i for i in range(n + 1)]
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x,y):
            par_x = find(x)
            par_y = find(y)
            if par_x == par_y:
                return False
            if rank[par_x] > rank[par_y]:
                parents[par_y] = par_x
                rank[par_x] += rank[par_y]
            else:
                parents[par_x] = par_y
                rank[par_y] += rank[par_x]
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1, n2]
        return []
            