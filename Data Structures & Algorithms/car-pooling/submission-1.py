class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
       	
        heap = [(trip[1], trip[2], trip[0]) for trip in trips]
        heapq.heapify(heap)
        curr = []
        dist = 0
        curr_taken = 0
        while heap:
            if not curr:
                dist = heap[0][0]
            while curr and curr[0][0] <= dist:
                item = heapq.heappop(curr)
                curr_taken -= item[2]
                
            while heap and heap[0][0] == dist:
                item = heapq.heappop(heap)
                curr_taken += item[2]
                heapq.heappush(curr, (item[1], item[0], item[2]))
                if curr_taken > capacity:
                    return False
            if heap and curr:
                dist = min(heap[0][0], curr[0][0])
            elif heap:
                dist = heap[0][0]
            else:
                break
        return True
