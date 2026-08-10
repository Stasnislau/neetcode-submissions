from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)
        time = 0
        q = deque([])
        while heap or q:
            if not heap:
                time = q[0][0]
            else:
                time += 1
            while q and q[0][0] <= time:
                heapq.heappush(heap,q.popleft()[1])
            if heap:
                val = heapq.heappop(heap) + 1
                if val != 0:
                    q.append((time + n + 1, val))
                    
        return time
            
