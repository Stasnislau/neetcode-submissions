from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        max_x = len(grid[0])
        max_y = len(grid)
        fresh = 0
        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == 2:
                    q.append((x,y))
                elif grid[y][x] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minute = 0
        directions = [(1,0), (-1,0),(0, 1), (0, -1)]
        while q and fresh > 0:
            minute += 1
            for _ in range(len(q)):
                (item_x, item_y) = q.popleft()
                for dx, dy in directions:
                    cx, cy = item_x + dx , item_y + dy
                    if 0 <= cx < max_x and 0 <= cy < max_y and grid[cy][cx] == 1:
                        grid[cy][cx] = 2
                        fresh -= 1
                        q.append((cx,cy))
        if fresh == 0:
            return minute
                    
        return -1
