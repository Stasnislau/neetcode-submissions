class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)



    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        if self.heap[0] > val:
            return self.heap[0]
        self.heap = [num * -1 for num in self.heap]
        if abs(self.heap[0]) <= val * -1:
            print(self.heap, self.heap[0], val)
            heapq.heappush(self.heap, val * -1)
            heapq.heappop(self.heap)
            self.heap = [num * -1 for num in self.heap]
            return self.heap[0]
        else:
            print(self.heap, self.heap[0], val)
            self.heap.append(val * -1)
            self.heap = [num * -1 for num in self.heap]
            heapq.heapify(self.heap)
            heapq.heappop(self.heap)
        return self.heap[0]


        
