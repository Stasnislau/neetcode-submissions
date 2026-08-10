from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for node in times:
            adj[node[0]].append((node[2], node[1]))
        visited = {k}
        heap = [(0, k)]
        time = 0
        while heap:
            if len(visited) == n:
                return time
            time = heap[0][0]
            item = heapq.heappop(heap)
            for tg in adj[item[1]]:
                if tg[1] not in visited:
                    heapq.heappush(heap,(time+tg[0], tg[1]))
            visited.add(item[1])  
                 

        return time if len(visited) == n else -1

        