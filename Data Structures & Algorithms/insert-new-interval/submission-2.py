class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        
        # ФАЗА 1: Левая зеленая зона.
        # Берем ВСЕ интервалы, которые заканчиваются строго ДО начала нашего нового интервала.
        # Они 100% не пересекаются, просто закидываем их в ответ.
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        # ФАЗА 2: Красная мясорубка (СЛИЯНИЕ).
        # Пока текущий интервал начинается ДО (или РАВНО) конца нашего нового интервала - ЕСТЬ ПЕРЕСЕЧЕНИЕ!
        # Мы НЕ пушим их в res! Мы берем наш newInterval и растягиваем его как гандон!
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0]) # Самое раннее начало
            newInterval[1] = max(newInterval[1], intervals[i][1]) # Самый поздний конец
            i += 1
            
        # Мясорубка закончилась. Пушим наш разбухший от слияний newInterval в ответ.
        res.append(newInterval)
        
        # ФАЗА 3: Правая зеленая зона.
        # Закидываем все оставшиеся интервалы. Они начинаются строго ПОСЛЕ нашего нового, 
        # пересечений больше быть не может.
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res
