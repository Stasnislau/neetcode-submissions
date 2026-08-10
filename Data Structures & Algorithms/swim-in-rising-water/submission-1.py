class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0, -1), (1,0),(-1,0)]
        visited = {(0,0)}
        heap = [(grid[0][0],0,0)]
        max_time = 0
        while heap:
            (time, cur_x, cur_y) = heapq.heappop(heap)
            max_time = max(time, max_time)
            if cur_x == len(grid) -1 and cur_y == len(grid) -1:
                return max_time
            for dx,dy in directions:
                cx, cy = cur_x + dx, cur_y + dy
                if 0 <= cx < len(grid) and 0 <= cy < len(grid) and (cx, cy) not in visited:
                    heapq.heappush(heap,(grid[cy][cx], cx, cy))    
                    visited.add((cx,cy))                    
        return max_time
