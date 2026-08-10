class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        actual_rotation = k % len(nums)
        if actual_rotation == 0:
            return
        nums.reverse()
        l = 0
        r = actual_rotation - 1
        
        def rotate(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        rotate(0 ,actual_rotation - 1)    
        rotate(actual_rotation, len(nums) - 1)


