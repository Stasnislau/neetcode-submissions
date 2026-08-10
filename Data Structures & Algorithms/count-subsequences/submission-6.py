class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)

        if m > n:
            return 0
        dp = [0] * (len(t) + 1)
        dp[0] = 1 
        for c in range(1, n + 1):
            for r in range(m, 0, -1):
                    if s[c-1] == t[r-1]:
                        dp[r] += dp[r-1]
        return dp[len(t)]