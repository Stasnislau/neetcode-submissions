from collections import deque
class MedianFinder:

    def __init__(self):
        self.right_min_heap = []
        self.left_max_heap = []
        self.medians = deque()

    def addNum(self, num: int) -> None:
        if self.right_min_heap and num >= self.right_min_heap[0]:
            heapq.heappush(self.right_min_heap, num)
            if len(self.right_min_heap) - len(self.left_max_heap) == 1:
                heapq.heappush(self.left_max_heap, -heapq.heappop(self.right_min_heap))
            return 
        heapq.heappush(self.left_max_heap, -num)
        if len(self.left_max_heap) - len(self.right_min_heap) == 2:
            heapq.heappush(self.right_min_heap, -heapq.heappop(self.left_max_heap))
        
        
        

    def findMedian(self) -> float:
        total_num = len(self.right_min_heap) + len(self.left_max_heap)
        print(self.left_max_heap, self.right_min_heap)
        return -self.left_max_heap[0] if total_num % 2 == 1 else (-self.left_max_heap[0] + self.right_min_heap[0]) / 2

        
        