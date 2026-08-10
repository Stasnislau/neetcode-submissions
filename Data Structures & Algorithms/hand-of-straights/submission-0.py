from collections import Counter
import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 1. Защита от дебила
        if len(hand) % groupSize != 0:
            return False
            
        # 2. Считаем сколько каждой карты у нас есть
        count = Counter(hand)
        
        # 3. Делаем хип ТОЛЬКО из уникальных карт, чтобы всегда быстро находить минимальную!
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        
        # 4. Крутим цикл, пока в хипе есть карты
        while min_heap:
            first = min_heap[0] # Берем минимальную карту, но пока не удаляем
            
            # Если эти карты мы уже все растратили в предыдущих группах - выкидываем из хипа
            if count[first] == 0:
                heapq.heappop(min_heap)
                continue
                
            # ЖАДНОСТЬ В ЧИСТОМ ВИДЕ СУКА! 
            # Эта карта ОБЯЗАНА начать группу от 'first' до 'first + groupSize - 1'
            for card in range(first, first + groupSize):
                # Если нужной следующей карты нет - всё, пиздец, стрит собрать нельзя!
                if count[card] == 0:
                    return False
                
                # Иначе "уничтожаем" (забираем со стола) эту карту для нашей группы
                count[card] -= 1
                
        return True
