from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0
        target = len(s) - 1
        if s[target] == '1':
            return False
        while q:
            i = q.popleft()
            min_reach = max(i + minJump, farthest)
            max_reach = min(i + maxJump, target)
            for j in range(min_reach, max_reach + 1):
                if j == target:
                    return True
                if s[j] == '0':
                    q.append(j)
            farthest = max(farthest, max_reach)
            
        return False