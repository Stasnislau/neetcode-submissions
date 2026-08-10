from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        count = 0
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum - k in sums:
                count += sums[curr_sum - k]
            sums[curr_sum] += 1
        return count