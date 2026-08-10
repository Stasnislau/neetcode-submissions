from typing import List
from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Убираем нули (они не дают профита) и ставим неубиваемые границы
        nums = [1] + [x for x in nums if x > 0] + [1]
        
        # Кэш для DP, чтобы не считать одно и то же
        @cache
        def dfs(l: int, r: int) -> int: # l и r - это открытые границы интервала
            if l > r:
                return 0
            
            # Перебираем КАЖДЫЙ шарик в интервале [l, r], предполагая, что он лопается ПОСЛЕДНИМ
            res = 0
            for i in range(l, r + 1):
                # Профит = (левая подзадача) + (правая подзадача) + (лопанье самого шарика 'i')
                # Когда лопается 'i', его соседями точно являются nums[l-1] и nums[r+1],
                # потому что всё внутри интервала уже лопнуло до него!
                coins = dfs(l, i - 1) + dfs(i + 1, r) + nums[l - 1] * nums[i] * nums[r + 1]
                res = max(res, coins)
                
            return res
            
        # Запускаем от первого до последнего РЕАЛЬНОГО шарика (без краев)
        return dfs(1, len(nums) - 2)
