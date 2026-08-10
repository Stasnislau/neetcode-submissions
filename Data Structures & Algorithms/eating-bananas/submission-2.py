import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles);
        mid = (l + r) // 2
        res = r
        while l <= r:
            mid = (l + r) // 2
            hoursTaken = 0
            for pile in piles:
                hoursTaken += math.ceil(pile/mid)
            if hoursTaken > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1

        return res
                
