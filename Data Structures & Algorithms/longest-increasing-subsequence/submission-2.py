class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        def helper(start):
            smallest = 0
            i = start - 1
            while i >= 0:
                if nums[start] > nums[i]:
                     smallest = max(smallest, dp[i])
                i -= 1
            return smallest 
        dp[0] = 1
        curr_start = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = 1 + helper(i)
            else:
                dp[i] = 1 + helper(i)
        print(dp)
        return max(dp)