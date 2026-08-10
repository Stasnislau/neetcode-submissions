from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        y_max = len(grid)
        x_max = len(grid[0])
        counter = 0
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        def bfs(x,y):
            q = deque([(x,y)]) 
            grid[y][x] = '0'
            
            while q:
                (curr_x, curr_y) = q.popleft()
                for dx, dy in directions:
                    tx, ty = curr_x + dx, curr_y + dy
                    if 0 <= tx < x_max and 0 <= ty < y_max and grid[ty][tx] != '0':
                        q.append((tx, ty))
                        grid[ty][tx] = '0'

        for y in range (y_max):
            for x in range(x_max):
                if grid[y][x] == '1':
                    bfs(x,y)
                    counter += 1

        return counter
