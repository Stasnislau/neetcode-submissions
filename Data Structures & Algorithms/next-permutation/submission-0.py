class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1 
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i 
                break
        if pivot == -1:
            nums.reverse()
            return
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        l = pivot + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


