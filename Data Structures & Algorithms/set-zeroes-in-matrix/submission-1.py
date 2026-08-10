class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False 
        
        # 1. СКАНИРОВАНИЕ (Размечаем нули по краям)
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # Метим столбец
                    if r > 0:
                        matrix[r][0] = 0 # Метим строку (если это не нулевая)
                    else:
                        rowZero = True # А если нулевая строка - зажигаем отдельный флаг!
                        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        # 3. ДОБИВАНИЕ КРАЕВ (Левый столбц)
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
