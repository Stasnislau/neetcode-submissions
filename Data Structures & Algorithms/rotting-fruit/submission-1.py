from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        max_x = len(grid[0])
        max_y = len(grid)
        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == 2:
                    grid[y][x] = -1
                    q.append((x,y))
                elif grid[y][x] == 1:
                    grid[y][x] = 0
                else:
                    grid[y][x] = -1
        directions = [(1,0), (-1,0),(0, 1), (0, -1)]
        print(grid)
        while q:
            (item_x, item_y) = q.popleft()
            for dx, dy in directions:
                cx, cy = item_x + dx , item_y + dy
                if 0 <= cx < max_x and 0 <= cy < max_y and grid[cy][cx] == 0:
                    grid[cy][cx] = max(grid[item_y][item_x],0) + 1
                    q.append((cx,cy))
        print(grid)
        res = 0
        for y in range(max_y):
            for x in range(max_x):
                    if grid[y][x] == 0:
                        return -1
                    elif grid[y][x] > 0:
                        res = max(res, grid[y][x])
                    
        return res
