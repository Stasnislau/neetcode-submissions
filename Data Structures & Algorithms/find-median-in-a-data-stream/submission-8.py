class MedianFinder:

    def __init__(self):
        self.right_min_heap = []
        self.left_max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_max_heap, -num)
        heapq.heappush(self.right_min_heap, -heapq.heappop(self.left_max_heap))
        if len(self.right_min_heap) > len(self.left_max_heap):
            heapq.heappush(self.left_max_heap, -heapq.heappop(self.right_min_heap))


    def findMedian(self) -> float:
        total_num = len(self.right_min_heap) + len(self.left_max_heap)
        return -self.left_max_heap[0] if total_num % 2 == 1 else (-self.left_max_heap[0] + self.right_min_heap[0]) / 2

        
        