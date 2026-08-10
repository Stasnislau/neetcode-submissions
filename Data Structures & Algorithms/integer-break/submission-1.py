class Solution:
    def integerBreak(self, n: int) -> int:
        # Базовые случаи, так как число ОБЯЗАТЕЛЬНО нужно разбить
        if n == 2: return 1
        if n == 3: return 2
        
        # Для n >= 4 выгоднее не разбивать куски 2 и 3, 
        # поэтому инициализируем dp[i] = i
        dp = [i for i in range(n + 1)]
        
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * j)
                
        return dp[n]
