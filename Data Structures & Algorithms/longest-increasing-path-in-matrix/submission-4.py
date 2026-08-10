from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1,0), (0,-1)]
        x_max, y_max = len(matrix[0]),len(matrix)
        if not matrix or not matrix[0]:
            return 0

        @cache
        def dfs(x,y):
            max_count = 1
            for dx, dy in directions:
                cx, cy = x + dx, y + dy
                if 0 <= cx < x_max and 0 <= cy < y_max and matrix[y][x] < matrix[cy][cx]:
                    max_count = max(max_count, 1 + dfs(cx,cy)) 
            return max_count
            
        return max([dfs(x,y) for x in range(x_max) for y in range(y_max)])

                




                
                