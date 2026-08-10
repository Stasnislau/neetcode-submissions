class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = 1
        while n <= len(nums):
            temp = nums[n-1]
            if temp != n and temp >= 1 and temp <= len(nums) and nums[temp-1] != temp:
                nums[temp-1], nums[n-1] = nums[n-1], nums[temp - 1]
            else:
                n += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1





        
        