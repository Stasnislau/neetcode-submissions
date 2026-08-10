class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        row = [False] * (len(s2) + 1)
        row[0] = True
        prev_row = [False] * (len(s2) + 1)

        
        for r in range(len(s1)+1):
            # print(row)
            for c in range(len(s2)+1):
                if c > 0 and s3[c+r - 1] == s2[c-1] and row[c-1]:
                    row[c] = True
                if r > 0 and s3[c+r - 1] == s1[r-1] and prev_row[c]:
                    row[c] = True
            print(row)
            prev_row = row
            row = [False] * (len(s2) + 1)
        return prev_row[-1]