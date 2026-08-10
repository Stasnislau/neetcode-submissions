from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        max_x = len(board[0])
        max_y = len(board)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for i in range(max_y):
            if board[i][0] == 'O':
                q.append((i, 0))
                board[i][0] = 'T'
            if board[i][max_x - 1] == 'O':
                board[i][max_x - 1] = 'T'
                q.append((i, max_x - 1))

        for i in range(1,max_x - 1):
            if board[0][i] == 'O':
                q.append((0, i))
                board[0][i] = 'T'
            if board[max_y-1][i] == 'O':
                q.append((max_y -1, i))
                board[max_y-1][i] = 'T'

        while q:
                item_y, item_x = q.popleft()
                if board[item_y][item_x] == 'X':
                    continue
                for dx, dy in directions:
                    cx, cy = dx + item_x, dy + item_y
                    if 0 <= cx < max_x and 0 <= cy < max_y and board[cy][cx] == 'O':
                        board[cy][cx] = 'T'
                        q.append((cy,cx))

        for y in range(max_y):
            for x in range(max_x):
                if board[y][x] == 'O':
                    board[y][x] = 'X'
                elif board[y][x] == 'T':
                    board[y][x] = 'O' 
                

