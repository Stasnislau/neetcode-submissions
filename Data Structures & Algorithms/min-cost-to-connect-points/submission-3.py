class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if j == i:
                    continue
                costs[i].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j))
        heap = []
        total_cost = 0
        visited = {0}
        heap = costs[0]
        heapq.heapify(heap)
        while heap:
            distance, j = heapq.heappop(heap)
            if j in visited:
                continue
            visited.add(j)
            total_cost += distance
            for val in costs[j]:
                heapq.heappush(heap, val)
        return total_cost


