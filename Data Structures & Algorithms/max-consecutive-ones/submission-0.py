class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            count += num
            if num == 0:
                count = 0
            res = max(count, res)
        return res