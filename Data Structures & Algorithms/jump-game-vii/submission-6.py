from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        checked = set()
        q = deque([0])
        target = len(s) - 1
        if s[target] == '1':
            return False
        while q:
            i = q.popleft()
            min_reach = i + minJump
            max_reach = i + maxJump
            if min_reach < target < max_reach:
                return True
            for j in range(min_reach, max_reach + 1):
                if j > target:
                    continue
                if j == target:
                    return True
                if j not in checked:
                    checked.add(j)
                    if s[j] == '0':
                        q.append(j)
                
        return False