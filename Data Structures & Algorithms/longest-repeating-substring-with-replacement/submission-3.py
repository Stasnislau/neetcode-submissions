from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)
        maxCount = 0
        localCount = 0
        r = 0
        counts = defaultdict(int)
        counts[s[0]] = 1

        for l in range(len(s)):
            
            maxF = max(counts.values())

            while maxF + k >= r - l + 1 and r < len(s) - 1:
                r += 1
                counts[s[r]] += 1
                maxF = max(counts.values())
                
            print(counts)
            maxCount = max(maxCount, maxF + k)
            counts[s[l]] -= 1
        return min(maxCount, len(s))   
                
