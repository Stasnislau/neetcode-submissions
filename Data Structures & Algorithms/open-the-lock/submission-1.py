from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque([('0000',0)])
        visited = set(deadends)
        if '0000' in visited:
            return -1
        while q:
            item, num = q.popleft()
            if item == target:
                return num
            for i in range(4):
                nei_down = item[:i] + str((int(item[i]) - 1) % 10) + item[i+1:]
                nei_up = item[:i] + str((int(item[i]) + 1) % 10) + item[i+1:]
                if nei_down not in visited:
                    visited.add(nei_down)
                    q.append((nei_down, num+1))
                if nei_up not in visited:
                    visited.add(nei_up)
                    q.append((nei_up, num + 1))
        return -1


        