class Solution:
    def insert(self, intervals, new):
        res = []
        i, n = 0, len(intervals)
        # ФАЗА 1: целиком ДО new (конец меньше начала new) → берём как есть
        while i < n and intervals[i][1] < new[0]:
            res.append(intervals[i]); i += 1
        # ФАЗА 2: пересекаются → сливаем ВСЕ в new
        while i < n and intervals[i][0] <= new[1]:
            new[0] = min(new[0], intervals[i][0])
            new[1] = max(new[1], intervals[i][1])
            i += 1
        res.append(new)
        # ФАЗА 3: целиком ПОСЛЕ → добираем хвост
        while i < n:
            res.append(intervals[i]); i += 1
        return res
