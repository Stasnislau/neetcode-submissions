class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_val = 0
        min_val = float('inf')
        for i in range(len(nums)):
            curr_val += nums[i]
            while curr_val >= target:
                min_val = min(i-l + 1, min_val)
                curr_val -= nums[l]
                l += 1
        return min_val if min_val != float('inf') else 0