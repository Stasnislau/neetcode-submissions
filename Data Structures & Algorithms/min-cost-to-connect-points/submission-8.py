class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [] 
        for j in range(len(points)):
            heapq.heappush(heap, (abs(points[0][0] - points[j][0]) + abs(points[0][1] - points[j][1]), j))
        total_cost = 0
        visited = {0}
        while heap:
            distance, j = heapq.heappop(heap)
            if j in visited:
                continue
            visited.add(j)
            total_cost += distance
            for i in range(len(points)):
                if i in visited:
                    continue
                heapq.heappush(heap, (abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1]), i))
            
        return total_cost


