class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        r = 0
        max_sum = nums[0]
        min_sum = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        total = sum(nums)
        while r < len(nums) - 1:
            if curr_max < 0:
                curr_max = 0
            if curr_min > 0:
                curr_min = 0
            r += 1
            
            curr_max += nums[r]
            curr_min += nums[r]

            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum