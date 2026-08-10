from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = defaultdict(int)
        res = [0, float('inf')] # start, length
        for c in t:
            needed[c] += 1
        l = 0
        neededLeft = len(needed)
        for r in range(len(s)):
            if s[r] in needed:
                needed[s[r]] -= 1
                if needed[s[r]] == 0:
                    neededLeft -= 1;
            while neededLeft == 0:
                if res[1] > r - l + 1:
                    res = [l, r - l + 1]
                if s[l] in needed:
                    needed[s[l]] += 1
                    if needed[s[l]] > 0:
                        neededLeft += 1
                l += 1
                
         
        return s[res[0]:res[0] + res[1]] if res[1] != float('inf') else ''


        