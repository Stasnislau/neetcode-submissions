class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                right += 1
                left -= 1
            return count
        final_count = 0
        for i in range(len(s)):
            final_count += helper(i, i)
            final_count += helper(i-1, i)
        return final_count
            
        