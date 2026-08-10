from collections import deque
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        def calc(i, curr_sum):
            if curr_sum == target:
                return True
            
            if i == len(nums) or  curr_sum > target:
                return False
            return calc(i+1, curr_sum + nums[i]) or calc(i+1, curr_sum)
        target = total_sum // 2
        curr_sum = 0
        return calc(0, 0)
