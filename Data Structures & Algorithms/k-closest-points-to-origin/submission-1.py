import math
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = defaultdict(list)
        for i, (x, y) in enumerate(points):
            distances[x**2 + y**2].append(i)
        print(distances)
        keys = list(distances.keys())
        heapq.heapify(keys)
        print(keys)
        res = []
        while k > 0:
            smallest = heapq.heappop(keys)
            for ind in distances[smallest]:
                res.append(points[ind])
                k -= len(distances[smallest])

        return res

        
        