class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        dp = [float('inf')] * m
        
        # БАГФИКС: Инициализируем нулём, чтобы не посчитать первую клетку дважды!
        dp[0] = 0
        
        for row in grid:
            dp[0] += row[0]
            for i in range(1, m):
                dp[i] = min(dp[i], dp[i-1])
                dp[i] += row[i]
                
        return dp[-1]
