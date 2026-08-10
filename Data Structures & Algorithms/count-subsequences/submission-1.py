class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not t: return 1
        if not s: return 0
        
        n, m = len(s), len(t)
        
        # 1. Починили твою инициализацию. Теперь это РАЗНЫЕ списки, сука!
        # Каждая запись будет: (индекс_в_s, количество_способов_дойти)
        res = [[] for _ in range(m)]
        
        # 2. Первый уровень (первый символ t)
        for c in range(n):
            if s[c] == t[0]:
                res[0].append([c, 1]) # Каждый первый символ дает 1 способ
        
        # 3. Последующие уровни
        for r in range(1, m):
            curr_char = t[r]
            for c in range(n):
                if s[c] == curr_char:
                    # Твоя "логика": ищем все способы из ПРЕДЫДУЩЕГО ряда, 
                    # где индекс меньше текущего c
                    ways_to_reach_c = 0
                    for prev_index, prev_ways in res[r-1]:
                        if prev_index < c:
                            ways_to_reach_c += prev_ways
                        else:
                            # Мы в s идем слева направо, можно было бы оптимизировать
                            break 
                    
                    if ways_to_reach_c > 0:
                        res[r].append([c, ways_to_reach_c])
            
            # Если на каком-то уровне символы не нашлись - всё, приехали
            if not res[r]:
                return 0
        
        return sum(ways for index, ways in res[-1])
