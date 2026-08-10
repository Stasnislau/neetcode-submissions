class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        has_taken_zero = False
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) - 1):
            curr = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = curr
        res1 = prev1
        prev2 = 0
        prev1 = 0
        for i in range(1, len(nums)):
            curr = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = curr
        return max(prev1, res1)
            
        