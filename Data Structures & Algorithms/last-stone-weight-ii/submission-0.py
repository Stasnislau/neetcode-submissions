class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s_sum = sum(stones)
        target = s_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for stone in stones:
            for i in range(target, stone - 1, -1):
                if dp[i - stone]:
                    dp[i] = True
                    
        res = 0
        for i in range(target, -1, -1):
            if dp[i]:
                res = i
                break
                
        return s_sum - (2 * res)
