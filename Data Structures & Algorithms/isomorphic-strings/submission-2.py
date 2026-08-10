class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i = 0
        changed = {}
        other = {}
        while i < len(s):
            if (s[i] in changed and changed[s[i]] != t[i]) or (t[i] in other and  other[t[i]] != s[i]):
                return False
            changed[s[i]] = t[i]
            other[t[i]] = s[i]
            i += 1
        return True