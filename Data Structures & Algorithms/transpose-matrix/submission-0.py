class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        new_matrix = [[0] * n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                new_matrix[i][j] = matrix[j][i]
        return new_matrix

