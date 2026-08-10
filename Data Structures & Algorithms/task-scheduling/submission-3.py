from collections import defaultdict, Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)
        time = 0
        q = deque([])
        print(heap)
        while heap or q:
            time += 1
            if heap:
                count = heapq.heappop(heap) + 1
                if count != 0:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
                    
                    
        return time
            
