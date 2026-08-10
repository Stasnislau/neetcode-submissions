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
                    options = [dp[r][c-1] + 1, dp[r-1][c-1] + 1]
                    dp[r][c] = min(options)
        return min([(dp[i][len(word1)] + (len(word2)) - i) for i in range(len(word2) + 1)])
