class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = [(capital[i], profits[i]) for i in range(len(profits))]
        available = []
        cap = w
        heapq.heapify(heap)
        for _ in range(k):
            while heap and heap[0][0] <= cap:
                heapq.heappush(available, -heapq.heappop(heap)[1])
            if available:
                cap -= heapq.heappop(available)
        return cap 

