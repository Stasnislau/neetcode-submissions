class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 101
        i = 0
        while i < len(prices):
            if minPrice < prices[i]:
                i += 1;
                continue
            j = i + 1;
            currentProfit = 0
            while j < len(prices):
                currentProfit = prices[j] - prices[i]
                maxProfit = max(currentProfit, maxProfit)
                j += 1
            i += 1;
        return maxProfit

