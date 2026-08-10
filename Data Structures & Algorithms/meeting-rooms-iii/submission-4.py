class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        heap = [(0, i) for i in range(n)]
        heapq.heapify(heap)
        counts = [0] * n
        max_count = 0
        for meet in meetings:
            while heap and heap[0][0] < meet[0]:
                heapq.heappushpop(heap, (meet[0], heap[0][1]))
            index = heap[0][1]
            counts[index] += 1
            max_count = max(max_count, counts[index])
            heapq.heappushpop(heap, (heap[0][0] + meet[1] - meet[0], heap[0][1]))
        return counts.index(max_count)




            