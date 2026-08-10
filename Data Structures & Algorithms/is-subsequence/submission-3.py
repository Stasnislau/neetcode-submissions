class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        def check_sub(start):
            j = 0
            i = start
            while j < len(s) and i < len(t):
                if s[j] == t[i]:
                    j += 1
                    i += 1
                else:
                    i += 1
            return j == len(s)
        res = False
        for i in range(len(t)):
            if t[i] == s[0]:
                res = check_sub(i)
            if res:
                return res
        return res
                

