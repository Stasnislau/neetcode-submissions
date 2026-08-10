import math

class Solution:
    def numSquares(self, n: int) -> int:
        opts = []
        for i in range(1, int(math.sqrt(n)) + 1):
            opts.append(i * i)
            
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for opt in opts:
                if opt > i:
                    break
                dp[i] = min(dp[i], dp[i - opt] + 1)
                
        return dp[n]
