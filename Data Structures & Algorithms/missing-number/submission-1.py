class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = nums[0]
        for i in range(1, len(nums)):
            total = total ^ nums[i] 
        for i in range(len(nums) + 1):
            total = total ^ i
        return total