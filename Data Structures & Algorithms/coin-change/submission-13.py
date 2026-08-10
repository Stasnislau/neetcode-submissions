class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        coins.sort()
        dp[0] = 0
        for coin in coins:
            if coin > amount:
                break
            dp[coin] = 1

        print(dp)
        for i in range(1, amount + 1):
            if dp[i] != -1:
                continue
            best = float('inf')
            for coin in coins:
                if i - coin < 0:
                    break
                if dp[i - coin] != -1:
                    best = min(best, dp[i-coin] + 1)
            if best != float('inf'):
                dp[i] = best
        return dp[amount]