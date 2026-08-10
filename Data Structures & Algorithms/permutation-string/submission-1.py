from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = defaultdict(int)
        if len(s1) > len(s2):
            return False
        l = 0
        for c1 in s1:
            counts[c1] += 1

        for r in range(len(s2)):
            counts[s2[r]] -= 1
            if max(counts.values()) == 0:
                return True
            if r - l + 1 >= len(s1):
                counts[s2[l]] += 1
                l += 1

        return False;