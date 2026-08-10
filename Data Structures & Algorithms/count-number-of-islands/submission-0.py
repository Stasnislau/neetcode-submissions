from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        y_max = len(grid)
        x_max = len(grid[0])
        self.counter = 0
        def bfs(x,y):
            q = deque([(x,y)])
            while q:
                (curr_x, curr_y) = q.popleft()
                grid[curr_y][curr_x] = '0'
                if curr_x - 1 >= 0 and grid[curr_y][ curr_x - 1] != '0':
                    q.append((curr_x - 1, curr_y))
                if curr_x + 1 != x_max and grid[curr_y][curr_x + 1] != '0':
                    q.append((curr_x + 1, curr_y))
                if curr_y - 1 >= 0 and grid[curr_y - 1][curr_x] != '0':
                    q.append((curr_x, curr_y - 1))
                if curr_y + 1 != y_max and grid[curr_y + 1][curr_x] != '0':
                    q.append((curr_x, curr_y + 1))
            self.counter += 1
                
        for y in range (y_max):
            for x in range(x_max):
                if grid[y][x] == '1':
                    print(y,x)
                    bfs(x,y)
        return self.counter
