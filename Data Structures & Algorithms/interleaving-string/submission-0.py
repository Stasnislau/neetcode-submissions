class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] *(len(s1) + 1) for _ in range(len(s2) + 1)]
        dp[len(s2)][len(s1)] = True
        print(dp)

        for c in range(len(s2), -1, -1):
            for r in range(len(s1), -1, -1):
                if c < len(s2) and s2[c] == s3[r + c] and dp[c+1][r]:
                    dp[c][r] = True
                if r < len(s1) and s1[r] == s3[r + c] and dp[c][r+1]:
                    dp[c][r] = True
        return dp[0][0]
            
            
        