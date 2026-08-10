class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        n = len(grid)
        m = len(grid[0])
        total = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    for dx, dy in directions:

                        if 0 <= x + dx < m and 0 <= y + dy < n and grid[y + dy][x + dx] == 0 or x + dx >= m or x + dx < 0 or y + dy >= n or 0 > y + dy:
                            total += 1
        return total
