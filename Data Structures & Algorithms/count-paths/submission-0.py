class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for x in range(n):
            for y in range(m):
                
                if x - 1 >= 0:
                    dp[y][x] += dp[y][x-1]
                if y - 1 >= 0:
                    dp[y][x] += dp[y-1][x]
        return dp[m-1][n-1]
                
        