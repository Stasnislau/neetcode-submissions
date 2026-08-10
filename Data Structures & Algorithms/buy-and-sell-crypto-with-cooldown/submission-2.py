class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -prices[0]
        rest = 0
        sold = float('-inf')

        for i in range(1,len(prices)):
            prev_hold = hold
            prev_rest = rest
            prev_sold = sold
            hold = max(prev_hold, prev_rest - prices[i])
            rest = max(prev_sold, prev_rest)
            sold = prev_hold + prices[i]
        return max(rest, sold)
