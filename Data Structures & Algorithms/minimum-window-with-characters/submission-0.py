from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = defaultdict(int)
        res = [0, float('inf')] # start, length
        for c in t:
            needed[c] += 1
        l = 0
        for r in range(len(s)):
            if s[r] in needed:
                needed[s[r]] -= 1
            print(needed)
            while max(needed.values()) <= 0 and r > l:
                if res[1] > r - l + 1:
                    res = [l, r - l + 1]
                if s[l] in needed:
                    needed[s[l]] += 1
                l += 1
            if max(needed.values()) <= 0 and res[1] > r - l + 1:
                res = [l, r - l + 1]
                
        print(res)
        if res[1] != float('inf'):
            return s[res[0]:res[0] + res[1]]   
        return ''


        