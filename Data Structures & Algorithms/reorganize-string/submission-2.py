from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-val, c) for c, val in count.items()]
        heapq.heapify(heap)
        res = []
        while len(heap) >= 2:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            res.append(first[1])
            res.append(second[1])
            if first[0] * -1 > 1:
                heapq.heappush(heap, (first[0] + 1, first[1]))
            if second[0] * -1 > 1:
                heapq.heappush(heap, (second[0] + 1, second[1]))
        if len(heap) > 1 or (heap and heap[0][0] < -1):
            return ""
        if heap:
            res.append(heap[0][1])
        return "".join(res)
