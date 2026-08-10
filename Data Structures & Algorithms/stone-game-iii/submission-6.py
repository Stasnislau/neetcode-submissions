class Solution:
      def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * n + [0] 
        for i in range(n-1, -1, -1):
            curr = 0
            opt = float('-inf')
            for j in range(1,4):
                if i + j - 1 < n:
                    curr += stoneValue[i+ j - 1]
                    opt = max(opt, curr - dp[i+j])
            dp[i] = opt
        if dp[0] == 0:
            return 'Tie'
        return 'Alice' if dp[0] > 0 else 'Bob'
                    
