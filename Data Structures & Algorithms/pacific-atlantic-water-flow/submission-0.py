from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1,0), (-1,0), (0, 1), (0,-1)]
        max_x = len(heights[0])
        max_y = len(heights)
        q_pac = deque([])
        q_atl = deque([])
        for i in range(max_x):
            q_pac.append((0,i))
            q_atl.append((max_y-1, i))
        for i in range(0,max_y):
            q_pac.append((i, 0))
            q_atl.append((i,max_x - 1))
        
        def bfs(q):
            res = set(q)
            while q:
                item_y, item_x = q.popleft()
                for dx,dy in directions:
                    cx, cy = dx + item_x, dy + item_y
                    if 0 <= cx < max_x and 0 <= cy < max_y:
                        if heights[item_y][item_x] <= heights[cy][cx] and (cy,cx) not in res:
                            res.add((cy,cx))
                            q.append((cy,cx))
            return res
        return list(bfs(q_atl).intersection(bfs(q_pac)))

                            
            


