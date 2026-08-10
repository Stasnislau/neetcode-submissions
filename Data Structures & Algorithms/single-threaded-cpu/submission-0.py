import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available_heap = []
        left_heap = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        heapq.heapify(left_heap)
        time = left_heap[0][0]
        res = []
        while left_heap or available_heap:
            if not available_heap and time < left_heap[0][0]:
                time = left_heap[0][0]
            while left_heap and left_heap[0][0] <= time:
                popped = heapq.heappop(left_heap)
                heapq.heappush(available_heap, (popped[1], popped[2]))
            if available_heap:
                popped_time, index = heapq.heappop(available_heap)
                time += popped_time
                res.append(index)
        return res
                




