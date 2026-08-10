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
            item_time, item_n = heapq.heappop(heap)
            visited.add(item_n)  
            for (tg_time, tg_num) in adj[item_n]:
                if tg_num not in visited:
                    heapq.heappush(heap,(time+tg_time, tg_num))

        return time if len(visited) == n else -1

        