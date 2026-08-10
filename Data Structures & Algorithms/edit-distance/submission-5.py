class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) > len(word1):
            word1, word2 = word2, word1
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        dp[0] = [i for i in range(len(word1) + 1)]
        for i in range(len(word2) + 1):
            dp[i][0] = i

        for r in range(1, len(word2) + 1):
            for c in range(1, len(word1) + 1):
                if word1[c-1] == word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
        return dp[len(word2)][len(word1)]
