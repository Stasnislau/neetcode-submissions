class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let max = 0;
        let prevMin = prices[0]
        for (let i = 1; i < prices.length; i++) {
            if (prices[i] - prevMin > max) {
                max = prices[i] - prevMin
            }
            if (prevMin > prices[i]) {
                prevMin = prices[i];
            }
        }
        return max
    }
}
