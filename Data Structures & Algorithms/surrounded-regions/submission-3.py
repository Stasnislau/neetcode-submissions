from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        max_x = len(board[0])
        max_y = len(board)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        to_be_deleted = set()

        for i in range(max_y):
            q.append((i, 0))
            q.append((i, max_x - 1))

        for i in range(1,max_x - 2):
            q.append((0, i))
            q.append((max_y -1, i))

        for y in range(1, max_y - 1):
            for x in range(1, max_x - 1):
                if board[y][x] == 'O':
                    to_be_deleted.add((y,x))

        while q:
                item_y, item_x = q.popleft()
                if board[item_y][item_x] == 'X':
                    continue
                for dx, dy in directions:
                    cx, cy = dx + item_x, dy + item_y
                    if 0 <= cx < max_x and 0 <= cy < max_y:
                        if board[cy][cx] == 'O' and (cy, cx) in to_be_deleted:
                            to_be_deleted.remove((cy, cx))
                            q.append((cy,cx))

        for item_y, item_x in to_be_deleted:
            board[item_y][item_x] = 'X'
                

