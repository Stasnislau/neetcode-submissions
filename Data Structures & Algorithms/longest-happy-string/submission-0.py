class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
             heapq.heappush(heap, (-c, 'c'))
        heapq.heapify(heap)
        while heap:
            first = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == first[1]:
                if not heap:
                    break
                second = heapq.heappop(heap)
                res.append(second[1])
                if second[0] < -1:
                    heapq.heappush(heap, (second[0] + 1, second[1]))
                heapq.heappush(heap, (first[0], first[1]))
            else:
                res.append(first[1])
                if first[0] < -1:
                    heapq.heappush(heap, (first[0] + 1, first[1]))
       

        return "".join(res)