class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)

        if m > n:
            return 0
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for r in range(1, len(t) + 1):
            for c in range(1,len(s) + 1):
                if s[c-1] == t[r-1]:
                    dp[r][c] = dp[r][c-1] + dp[r-1][c-1]
                else:
                    dp[r][c] = dp[r][c-1]
        print(dp)
        return dp[len(t)][len(s)]