from typing import List
from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x > 0] + [1]
        
        @cache
        def dfs(l,r):
            if l > r:
                return 0
            res = 0
            for i in range(l, r + 1):
                val = nums[i] * nums[l-1] * nums[r+1] + dfs(l, i -1) + dfs(i+1,r)
                res = max(val, res)
            return res
        return dfs(1, len(nums) - 2)