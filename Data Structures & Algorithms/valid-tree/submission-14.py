from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        rank = [1] * n 
        parents = [i for i in range(n)] 
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x,y):
            x_par = find(x)
            y_par = find(y)
            if x_par == y_par:
                return False
            if rank[x_par] > rank[y_par]:     
                parents[find(y_par)] = x_par
                rank[x_par] += rank[y_par]
            else:
                parents[x_par] = y_par
                rank[y_par] += rank[x_par]
            return True
        components = n

        for n1,n2 in edges:
            if not union(n1,n2):
                return False
            components -= 1
        # return max(rank) == n
        return components == 1