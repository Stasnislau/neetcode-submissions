from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = sum(nums)
        sums = defaultdict(int)
        sums[nums_sum] = 1
        for num in nums:
            for el, val in list(sums.items()):
                curr_sum = el - num * 2
                sums[curr_sum] += val
        return sums[target]


            



