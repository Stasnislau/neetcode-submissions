class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)

        if m > n:
            return 0
        dp = [0] * (m + 1)
        dp[0] = 1

        for char_s in s:
            for j in range(m, 0, -1):
                if char_s == t[j-1]:
                    dp[j] += dp[j-1]
        return dp[m]
