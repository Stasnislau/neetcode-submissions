class UnionFind:
    def __init__(self, size):
        self.par = [i for i in range(size)]
        self.rank = [1] * size
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)
        if par_x == par_y:
            return False
        if self.rank[par_x] > self.rank[par_y]:
            self.rank[par_x] += self.rank[par_y]
            self.par[par_y] = par_x
        else:
            self.rank[par_y] += self.rank[par_x]
            self.par[par_x] = par_y
        return True
        

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key = lambda e: e[2])
        mst_weight = 0
        uf = UnionFind(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w
        critical, pseudo = [], []
        for n1, n2, e_weight, i in edges:
            weight = 0
            uf = UnionFind(n)
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue
            
            uf = UnionFind(n)
            uf.union(n1, n2)
            weight = e_weight
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)


        return [ critical, pseudo ]


         
