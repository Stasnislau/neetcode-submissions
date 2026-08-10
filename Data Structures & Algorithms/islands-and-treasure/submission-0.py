from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        max_x = len(grid[0])
        max_y = len(grid)
        def bfs(x, y):
            visited = set((x,y))
            print(visited)
            q = deque([(x,y,0)])
            directions = [(-1, 0), (1,0), (0, -1), (0,1)]
            while q:
                (item_x, item_y, curr_level) = q.popleft()
                for dx, dy in directions:
                    cx, cy = item_x + dx, item_y + dy
                    if 0 <= cx < max_x and 0 <= cy < max_y and grid[cy][cx] > 0 and (cx,cy) not in visited:
                        grid[cy][cx] = min(grid[cy][cx], curr_level+1)
                        visited.add((cx,cy))
                        q.append((cx,cy,curr_level+1))

        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == 0:
                    bfs(x,y)
        return