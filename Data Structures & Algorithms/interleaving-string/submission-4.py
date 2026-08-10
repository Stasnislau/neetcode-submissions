class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        print(dp)
        for r in range(len(s1)+1):
            for c in range(len(s2)+1):
                if c > 0 and s3[c+r - 1] == s2[c-1] and dp[r][c-1]:
                    dp[r][c] = True
                if r > 0 and s3[c+r - 1] == s1[r-1] and dp[r-1][c]:
                    dp[r][c] = True
        print(dp)
        return dp[len(s1)][len(s2)]