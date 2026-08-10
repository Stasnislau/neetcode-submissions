class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = nums[0]
        start_val = nums[0]
        for i in range(1, len(nums)):
            start_val -= 1
            if start_val < 0:
                return False
            if nums[i] > start_val:
                start_val = nums[i]
        return True
