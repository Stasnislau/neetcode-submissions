class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                curr = 0
            curr += nums[i]
            res = max(res, curr)
        return res