class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[1] * n for i in range(n)]
        left = 0
        right = n
        up = 0
        down = n
        curr_number = 1
        while left < right and up < down:
            for i in range(left, right):
                matrix[up][i] = curr_number
                curr_number += 1
            up += 1

            for i in range(up, down):
                matrix[i][right - 1] = curr_number
                curr_number += 1
            right -= 1

            # if left >= right or up >= down:
            #     break

            for i in range(right - 1, left - 1, -1):
                matrix[down - 1][i] = curr_number
                curr_number += 1
            down -= 1

            for i in range(down - 1, up - 1, -1):
                matrix[i][left] = curr_number
                curr_number += 1
            left += 1

            
        return matrix