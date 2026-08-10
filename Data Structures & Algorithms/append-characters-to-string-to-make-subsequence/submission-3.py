class Solution:
    def appendCharacters(self, s: str, t: str) -> bool:
        if not s:
            return len(t)
        res = 0
        def check_sub(start):
            j = 0
            i = start
            while j < len(t) and i < len(s):
                if s[i] == t[j]:
                    j += 1
                    i += 1
                else:
                    i += 1
            return j
        for i in range(len(s)):
            if s[i] == t[0]:
                res = max(res, check_sub(i))
        return len(t) - res
                

