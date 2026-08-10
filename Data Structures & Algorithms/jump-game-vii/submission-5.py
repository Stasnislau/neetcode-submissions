from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        checked = set()
        q = deque([0])
        max_reach = 0
        target = len(s) - 1
        if s[target] == '1':
            return False
        while q:
            i = q.popleft()
            max_reach = max(max_reach, i + minJump)
            for j in range(max_reach, i + maxJump + 1):
                if j > target:
                    continue
                if j == target:
                    return True
                if j not in checked:
                    checked.add(j)
                    if s[j] == '0':
                        q.append(j)
                
        return False