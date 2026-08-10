class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        def helper(left, right):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    return s[left+1: right]
            return s[left+1: right]

        for i in range(len(s)):
            res = helper(i-1, i)
            res2 = helper(i, i)
            if len(res) < len(res2):
                res = res2
            if len(res) > len(longest):
                longest = res
            

        return longest