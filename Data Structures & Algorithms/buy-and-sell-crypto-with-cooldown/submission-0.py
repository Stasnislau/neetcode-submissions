class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        # Базовые случаи для ПЕРВОГО дня (день 0):
        # Если в 1-й день мы купили акцию, значит наша прибыль ушла в минус:
        hold = -prices[0]
        # В 1-й день мы не можем ничего продать (мы еще ничего не купили)
        sold = float('-inf')
        # Если мы в 1-й день отдыхаем, наша прибыль 0
        rest = 0
        
        for i in range(1, len(prices)):
            # Обязательно сохраняем вчерашние значения перед обновлением!
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            
            # Обновляем состояния по нашим гениальным формулам:
            hold = max(prev_hold, prev_rest - prices[i])
            sold = prev_hold + prices[i]
            rest = max(prev_rest, prev_sold)
            
        # В самом конце (в последний день) максимум прибыли точно не может быть
        # в состоянии HOLD (зачем держать акцию в конце мира?).
        # Значит, максимальные бабки лежат либо в SOLD, либо в REST.
        return max(sold, rest)
