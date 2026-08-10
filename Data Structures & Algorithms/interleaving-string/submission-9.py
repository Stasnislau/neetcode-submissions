class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        row = [False] * (len(s2) + 1)

        
        for r in range(len(s1)+1):
            for c in range(len(s2)+1):
                if c == 0 and r == 0:
                    row[0] = True
                elif c == 0:
                    row[c] = s3[c+r - 1] == s1[r-1] and row[c]
                elif r == 0:
                    row[c] = s3[c+r - 1] == s2[c-1] and row[c-1]
                else:
                    row[c] = s3[c+r - 1] == s2[c-1] and row[c-1] or s3[c+r - 1] == s1[r-1] and row[c]
        return row[-1]