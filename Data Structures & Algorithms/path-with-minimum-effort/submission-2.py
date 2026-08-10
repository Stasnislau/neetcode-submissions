class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        heap = [(0,0,0)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        while heap:
            curr_max, curr_x, curr_y = heapq.heappop(heap)
            if curr_y == n - 1 and curr_x == m - 1:
                return curr_max
            if (curr_x, curr_y) in visited:
                continue
            visited.add((curr_x, curr_y))
            for dir_x, dir_y in directions:
                tx, ty = curr_x + dir_x, curr_y + dir_y
                if 0 <= tx < m and 0 <= ty < n and (tx, ty) not in visited:
                    new_max = max(curr_max, abs(heights[ty][tx] - heights[curr_y][curr_x]))
                    heapq.heappush(heap, (new_max, tx, ty))
        return -1