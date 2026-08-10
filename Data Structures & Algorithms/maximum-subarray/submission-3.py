class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 0
        max_sum = nums[0]
        curr_sum = nums[0]
        while r < len(nums) - 1:
            if curr_sum < 0:
                curr_sum = 0
            r += 1
            curr_sum += nums[r]
            max_sum = max(curr_sum, max_sum)
        return max_sum


