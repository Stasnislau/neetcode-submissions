from collections import defaultdict, deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for node in times:
            adj[node[0]].append((node[2], node[1]))
        visited = {k}
        time = -1
        heap = [(0, k)]
        while heap:
            time += 1
            while heap and heap[0][0] == time:
                item = heapq.heappop(heap)
                for tg in adj[item[1]]:
                    if tg[1] not in visited:
                        heapq.heappush(heap,(time+tg[0], tg[1]))
                visited.add(item[1])  
            if len(visited) == n:
                return time            

        return time if len(visited) == n else -1

        