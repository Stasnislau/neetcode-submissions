class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.area_sum = matrix
        for n in range(len(matrix)):
            for m in range(1, len(matrix[0])):
                self.area_sum[n][m] += self.area_sum[n][m -1]
        for n in range(len(matrix)):
            for m in range(len(matrix[0])):
                top = 0 if n == 0 else self.area_sum[n - 1][m]
                self.area_sum[n][m] += top
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = 0 
        top = 0
        cross = 0
        if row1 != 0:
            top = self.area_sum[row1-1][col2]
        if col1 != 0:
            left = self.area_sum[row2][col1-1]
        if col1 != 0 and row1 != 0:
            cross = self.area_sum[row1-1][col1-1]
        return self.area_sum[row2][col2] - top - left + cross


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)