from collections import defaultdict, deque
from typing import List
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Инициализация всех уникальных букв (ТВОЙ КОД, ОН ИДЕАЛЕН)
        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adj}
        # СТРОИМ ГРАФ КАК МУЖИКИ
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # ПРОВЕРКА НА БЛЯДСКИЙ ПРЕФИКС!
            # Если w1 длиннее w2 и w1 начинается с w2 (w1[:min_len] == w2)
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return "" # Это противоречие, алфавит говно!
            # Ищем ПЕРВУЮ несовпадающую букву
            for j in range(min_len):
                if w1[j] != w2[j]:
                    # Если мы ЕЩЁ НЕ добавляли это правило
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])    # Стрелка от w1[j] к w2[j]
                        indegree[w2[j]] += 1     # У w2[j] стало на одно правило БОЛЬШЕ
                    
                    # ПРАВИЛО НАЙДЕНО. ДАЛЬШЕ НЕ СМОТРИМ! ПО ТОРМОЗАМ!
                    break
        
        res = []
        q = deque()
        for key, val in indegree.items():
            if val == 0:
                q.append(key)
        while q:
            item = q.popleft()
            for nei in adj[item]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            res.append(item)
        if len(res) != len(list(adj.keys())):
            return ''
        return "".join(res)


        
