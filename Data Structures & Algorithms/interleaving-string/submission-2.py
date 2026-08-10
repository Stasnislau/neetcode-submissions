class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        for r in range(len(s1),-1,-1):
            for c in range(len(s2), -1,-1):
                if c < len(s2) and s3[c+r] == s2[c] and dp[r][c+1]:
                    dp[r][c] = True
                if r < len(s1) and s3[c+r] == s1[r] and dp[r+1][c]:
                    dp[r][c] = True

            
        return dp[0][0]