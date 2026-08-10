class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = [[float('-inf')] * len(piles) for _ in range(len(piles))]
        def rec(start, m, curr_sum):
            if start == len(piles):
                return 0
            if start + 2 * m >= len(piles):
                return curr_sum
            if m < len(piles) and dp[start][m] != float('-inf'):
                return dp[start][m]
            curr_val = 0
            for i in range(start,start + 2 * m):
                if i == len(piles):
                    break
                curr_val += piles[i]
                dp[start][m] = max(dp[start][m], curr_sum - rec(i+1, max(i - start + 1, m), curr_sum - curr_val))
            return dp[start][m]
        res = rec(0,1,sum(piles))
        print(dp)
        return res