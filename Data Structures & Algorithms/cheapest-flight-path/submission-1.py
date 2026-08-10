from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        prices = [float('inf')] * n
        prices[src] = 0
        print(prices)
        for i in range(k+1):
            temp_prices = prices[:]
            for fl_src, fl_dst, fl_price in flights:
                print(fl_src, fl_dst, fl_price)
                if prices[fl_src] != float('inf'):
                    temp_prices[fl_dst] = min(prices[fl_src] + fl_price, temp_prices[fl_dst])
            prices = temp_prices
            print(temp_prices)
            
        return prices[dst] if prices[dst] != float('inf') else -1

