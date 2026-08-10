class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        dp = [0] * m
        # Стартовая клетка: 1 путь, если нет камня, иначе 0
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for row in obstacleGrid:
            for j in range(m):
                if row[j] == 1:
                    # Если камень — сюда прийти нельзя, 0 путей
                    dp[j] = 0
                elif j > 0:
                    # dp[j] сейчас хранит значение СВЕРХУ (с прошлой итерации)
                    # dp[j-1] хранит значение СЛЕВА (уже обновлённое на этой итерации)
                    dp[j] += dp[j - 1]
                    
        return dp[-1]
