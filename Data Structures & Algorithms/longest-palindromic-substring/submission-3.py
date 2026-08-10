class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        start = 0
        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            res1 = helper(i-1, i)
            res2 = helper(i, i)
            res = max(res1, res2)
            if res > longest:
                start = i - (res // 2)
                longest = res
            print(res, i, start, longest )
            
            

        return s[start: start + longest]