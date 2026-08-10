class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(x, n):

            if n == 0:
                return 1
            val = calculate(x, n // 2)
            if n & 1 == 1:
                return x * val * val
            else:
                return val * val
        if n < 0:
            x = 1 / x
            n = -n
        return calculate(x,n)