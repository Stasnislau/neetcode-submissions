class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted((q, index) for index, q in enumerate(queries))
        res = [-1] * len(queries)
        for q, ind in sorted_queries:
            heap = []
            j = 0
            while j < len(intervals):
                if intervals[j][0] <= q <= intervals[j][1]:
                    heapq.heappush(heap, intervals[j][1] - intervals[j][0] + 1)
                j += 1
            if heap:
                res[ind] = heap[0]
        return res