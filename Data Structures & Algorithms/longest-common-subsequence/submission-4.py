from collections import defaultdict
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        r_len = len(text1) + 1
        c_len = len(text2) + 1
        row = [0 for _ in range(r_len)]
        res = 0
        for c in range(1, c_len):
            new_row = [0] * r_len
            for r in range(1, r_len):
                if text1[r - 1] == text2[c - 1]:
                    new_row[r] = 1 + row[r-1]
                else:
                    new_row[r] = max(row[r], new_row[r-1])
                res = max(res, new_row[r])
            row = new_row
            
        return res