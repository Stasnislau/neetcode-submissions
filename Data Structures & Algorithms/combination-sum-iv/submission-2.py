class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                if i - num == 0:
                    dp[i] += 1
                    continue
                dp[i] += dp[i - num]
                
        return dp[target]