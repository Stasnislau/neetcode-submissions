from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        rank = [1] * n 
        parents = [i for i in range(n)] 
        def find(x):
            if parents[x] != x:
                return find(parents[x])
            return x
        def union(x,y):
            x_par = find(x)
            y_par = find(y)
            if x_par == y_par:
                return
            if rank[x_par] > rank[y_par]:     
                parents[find(y_par)] = find(x_par)
                rank[x_par] = rank[x_par] + rank[y_par]
                rank[y_par] = 0
            else:
                parents[x_par] = find(y_par)
                rank[y_par] = rank[x_par] + rank[y_par]
                rank[x_par] = 0


        for n1,n2 in edges:
            if find(n1) == find(n2):
                return False
            union(n1,n2)

        return max(rank) == n



            