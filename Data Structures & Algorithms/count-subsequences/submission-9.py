class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)
        cache = {}

        # if m > n:
        #     return 0
        # dp = [0] * (m + 1)
        # dp[0] = 1 
        # for c in range(1, n + 1):
        #     for r in range(m, 0, -1):
        #             if s[c-1] == t[r-1]:
        #                 dp[r] += dp[r-1]
        # return dp[len(t)]
        def rec(i, j):
            if j == m:
                return 1
            if i == n:
                return 0
            if (i, j) in cache:
                return cache[(i,j)]
            if s[i] == t[j]:
                cache[(i,j)] = rec(i+1,j) + rec(i+1, j+1)
            else:
                cache[(i,j)] = rec(i+1,j)
            return cache[(i,j)]
        return rec(0,0)