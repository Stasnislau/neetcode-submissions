class Solution:
    def scoreOfString(self, s: str) -> int:
        running_sum = 0
        for i in range(1, len(s)):
            running_sum += (abs(ord(s[i]) - ord(s[i-1])))
        return running_sum