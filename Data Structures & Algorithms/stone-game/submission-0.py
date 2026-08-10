class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[float('-inf')] * n for _ in range(n)]
        
        def diff(start, end):
            if start > end:
                return 0
                
            if dp[start][end] != float('-inf'):
                return dp[start][end]
                
            # Minimax: Мои очки МИНУС максимальное преимущество противника на следующем ходу
            opt1 = piles[start] - diff(start + 1, end)
            opt2 = piles[end] - diff(start, end - 1)
            
            dp[start][end] = max(opt1, opt2)
            return dp[start][end]
            
        # Возвращаем True, если Алиса (первый игрок) может получить преимущество > 0
        return diff(0, n - 1) > 0
