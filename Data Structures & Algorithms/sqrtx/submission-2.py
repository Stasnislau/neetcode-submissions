class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = math.floor((l + r) / 2)
            total = mid * mid
            if total == x:
                return mid
            elif total > x:
                r = mid - 1
            else:
                l = mid + 1
        return r