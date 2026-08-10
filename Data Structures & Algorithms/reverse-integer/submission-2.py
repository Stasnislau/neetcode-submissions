class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647
        
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            ones = x % 10
            x = x // 10
            
            if res > MAX // 10 or (MAX // 10 == res and ones > 7 ):
                return 0
            res = res * 10 + ones
        return sign * res
