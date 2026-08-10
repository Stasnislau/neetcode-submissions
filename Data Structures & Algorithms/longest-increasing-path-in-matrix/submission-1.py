from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1,0), (0,-1)]
        dp = [[1] * len(matrix[0]) for _ in range(len(matrix))]
        visited = set()
        x_max = len(matrix[0])
        y_max = len(matrix)
        res = 0
        def dfs(x,y, count):
            max_count = count
            visited.add((x,y))
            for dx, dy in directions:
                cx, cy = x + dx, y + dy
                if 0 <= cx < x_max and 0 <= cy < y_max and matrix[y][x] < matrix[cy][cx]:
                    print( matrix[y][x], matrix[cy][cx])
                    if not (cx,cy) in visited:
                        max_count = max(max_count, dfs(cx,cy, count + 1)) 
                    else:
                        max_count = max(max_count, count + dp[cy][cx])
            dp[y][x] = max(dp[y][x], max_count - count + 1)
            return max_count
                

        for y in range(y_max):
            for x in range(x_max):
                if (x,y) not in visited:
                    res = max(res, dfs(x,y, 1))
                else:
                    res = max(res, dp[y][x])
        return res
                




                
                