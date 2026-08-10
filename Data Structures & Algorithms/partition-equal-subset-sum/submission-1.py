from collections import deque
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum // 2
        sums = set()
        for num in nums:
            temp = sums.copy()
            for el in temp:
                sums.add(el+num)
            sums.add(num)
        
        return target in sums
