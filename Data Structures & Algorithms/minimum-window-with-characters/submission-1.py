class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = defaultdict(int)
        for c in t: needed[c] += 1
            
        res = [0, float('inf')] # start, length
        l = 0
        
        # Чтобы не крутить max() каждый раз, 
        # введем переменную "сколько уникальных букв еще нужно удовлетворить"
        # Это оптимизация O(N), как в прошлой задаче.
        needed_count = len(needed) 
        
        for r in range(len(s)):
            char = s[r]
            
            # Если буква есть в T, уменьшаем ее счетчик
            if char in needed:
                needed[char] -= 1
                # Если счетчик стал 0 (ровно столько, сколько надо) - одна буква закрыта
                if needed[char] == 0:
                    needed_count -= 1
            
            # Пока все уникальные буквы закрыты (окно валидно)
            while needed_count == 0:
                # 1. Пробуем обновить рекорд (окно [l:r+1])
                curr_len = r - l + 1
                if curr_len < res[1]:
                    res = [l, curr_len]
                
                # 2. Сжимаем слева
                left_char = s[l]
                if left_char in needed:
                    needed[left_char] += 1
                    # Если счетчик стал положительным (0 -> 1), 
                    # значит нам снова не хватает этой буквы
                    if needed[left_char] > 0:
                        needed_count += 1
                
                l += 1
                
        start, length = res
        return s[start : start + length] if length != float('inf') else ""