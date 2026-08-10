from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        max_x = len(grid[0])
        max_y = len(grid)
        q = deque()
        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == 0:
                    q.append((x,y))
        directions = [(-1, 0), (1,0), (0, -1), (0,1)]
        while q:
            (item_x, item_y) = q.popleft()
            for dx, dy in directions:
                cx, cy = item_x + dx, item_y + dy
                if 0 <= cx < max_x and 0 <= cy < max_y and grid[cy][cx] > 0 and grid[cy][cx] == 2147483647:
                    grid[cy][cx] = grid[item_y][item_x] + 1
                    q.append((cx,cy))

        return