from collections import defaultdict
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r_len = len(text1) + 1
        c_len = len(text2) + 1
        dp = [[0 for _ in range(r_len)] for _ in range(c_len)]
        res = 0
        for c in range(1, c_len):
            for r in range(1, r_len):
                print(text1[r - 1], text2[c - 1])
                if text1[r - 1] == text2[c - 1]:
                    dp[c][r] = 1 + dp[c-1][r-1]
                else:
                    dp[c][r] = max(dp[c-1][r], dp[c][r-1])
                res = max(res, dp[c][r])
        print(dp)
        return res