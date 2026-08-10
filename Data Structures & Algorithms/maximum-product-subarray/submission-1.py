class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            
            temp_max = curr_max
            curr_max = max(curr_max * nums[i], curr_min * nums[i], nums[i])
            curr_min = min(temp_max * nums[i], curr_min * nums[i], nums[i])
            res = max(res, curr_max)
        return res