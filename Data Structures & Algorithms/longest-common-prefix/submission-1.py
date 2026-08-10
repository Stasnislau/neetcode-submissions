class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) < 2:
            return strs[0]
        comp = strs[0]
        for i in range(len(comp)):
            for s in strs[1:]:
                if i == len(s) or comp[i] != s[i]:
                    return comp[:i]
        return comp
            