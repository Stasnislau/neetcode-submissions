from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x > 0] + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]
    
        for length in range(1, len(nums) - 1):
            for l in range(1, len(nums) - length):
                r = l + length - 1
                max_coins = 0
                for i in range(l, r+1):
                    coins = nums[l-1]*nums[i]*nums[r+1] + dp[l][i-1] + dp[i+1][r]
                    max_coins = max(coins, max_coins)
                dp[l][r] = max_coins
        return dp[1][len(nums)-2]
        
                    
