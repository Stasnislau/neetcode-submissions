class Solution:
      def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] хранит то же самое, но мы идём с КОНЦА в НАЧАЛО
        dp = [float('-inf')] * n + [0] # dp[n] = 0
        
        for i in range(n - 1, -1, -1):
            score = 0
            ans = float('-inf')
            for j in range(1, 4):
                if i + j - 1 < n:
                    score += stoneValue[i + j - 1]
                    ans = max(ans, score - dp[i + j])
            dp[i] = ans
            
        diff = dp[0]
        if diff > 0: return "Alice"
        if diff < 0: return "Bob"
        return "Tie"