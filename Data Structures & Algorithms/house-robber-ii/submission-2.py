class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            prev2 = 0
            prev1 = 0
            for i in range(len(nums)):
                curr = max(prev2 + nums[i], prev1)
                prev2 = prev1
                prev1 = curr
            return prev1
        
        return max(helper(nums[1:]), helper(nums[:-1]))
            
        