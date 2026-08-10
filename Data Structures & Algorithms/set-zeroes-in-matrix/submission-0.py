class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cols = set()
        rows = set()
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    cols.add(y)
                    rows.add(x)
        for y in cols:
            matrix[y] = [0] * len(matrix[0])
        for x in rows:
            for i in range(len(matrix)):
                matrix[i][x] = 0