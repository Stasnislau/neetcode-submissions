import math
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            val = x**2 + y**2
            if len(res) < k:
                heapq.heappush(res, (-val,x,y))
            elif res[0][0] < -val:
                heapq.heappushpop(res, (-val, x,y))

        return [[x,y] for _, x, y in res]

        
        