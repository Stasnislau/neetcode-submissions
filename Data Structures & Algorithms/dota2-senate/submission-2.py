from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque()
        dq = deque()
        n = len(senate)
        for i, c in enumerate(senate):
            if c == 'R':
                rq.append(i)
            else:
                dq.append(i)
        while rq and dq:
            ri = rq.popleft()
            di = dq.popleft()
            if ri < di:
                rq.append(ri + n)
            else:
                dq.append(di + n)
        
        return 'Radiant' if len(rq) > 0 else 'Dire'