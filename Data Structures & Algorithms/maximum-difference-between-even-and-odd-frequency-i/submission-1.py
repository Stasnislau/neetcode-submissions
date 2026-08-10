class Solution:
    def maxDifference(self, s: str) -> int:
        alph = [0] * 26
        for c in s:
            index = ord(c) - 97
            alph[index] += 1
        max_odd = 0
        min_even = len(s)
        for c in alph:
            if c == 0:
                continue
            if c % 2:
                max_odd = max(max_odd, c)
            else:
                min_even = min(min_even, c)
        return max_odd - min_even