class Solution:
    def appendCharacters(self, s: str, t: str) -> bool:
        if not s:
            return len(t)
        res = 0
        i = 0
        j = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                j += 1
                i += 1
            else:
                i += 1
        return len(t) - j
                

