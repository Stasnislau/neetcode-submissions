class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = [i for i in range(len(points))]
        rank = [1] * len(points)
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x,y):
            par_x = find(x)
            par_y = find(y)
            if par_x == par_y:
                return False
            if rank[par_x] >= rank[par_y]:
                rank[par_x] += rank[par_y]
                parents[par_y] = par_x
            else:
                rank[par_y] += rank[par_x]
                parents[par_x] = par_y
            return True
        
        heap = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                heap.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j, ))
        heapq.heapify(heap)
        taken = 0
        total_sum = 0
        while taken + 1 != len(points):
            distance, i, j = heapq.heappop(heap)
            if union(i,j):
                taken += 1
                total_sum += distance
        return total_sum
            



