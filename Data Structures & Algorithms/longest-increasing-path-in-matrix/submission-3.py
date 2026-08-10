class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1,0), (0,-1)]
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        x_max = len(matrix[0])
        y_max = len(matrix)
        res = 0
        def dfs(x,y):
            max_count = 1
            if dp[y][x] != 0:
                return dp[y][x]
            for dx, dy in directions:
                cx, cy = x + dx, y + dy
                if 0 <= cx < x_max and 0 <= cy < y_max and matrix[y][x] < matrix[cy][cx]:
                    max_count = max(max_count, 1 + dfs(cx,cy)) 
            dp[y][x] = max_count
            return max_count
                

        for y in range(y_max):
            for x in range(x_max):
                res = max(res, dfs(x,y))
        return res
                




                
                