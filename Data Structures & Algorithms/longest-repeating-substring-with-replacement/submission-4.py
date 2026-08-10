from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)
        maxCount = 0
        l = 0
        counts = defaultdict(int)
        

        for r in range(len(s)):
            counts[s[r]] += 1
            maxF = max(counts.values())
            while r - l + 1 > maxF + k:
                counts[s[l]] -= 1
                l += 1
                maxF = max(counts.values())
            maxCount = max(maxCount, r - l + 1)
        return maxCount