
class Solution:
    def check_if_y_allowed(self, curr_board, y):
        return 'Q' not in curr_board[y] 
    def check_diagonal_allowed(self, curr_board, x,y):
        y1, y2 = y,y
        while x >= 0:
            if y1 >= 0:
                if curr_board[y1][x] == 'Q':
                    return False
            if y2 < len(curr_board):
                if curr_board[y2][x] == 'Q':
                    return False
            x -= 1
            y1 -= 1
            y2 += 1
        return True
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtracking(x, curr_board):
            if x == n:
                res.append(curr_board[:])
                return
            for y in range(n):
                if self.check_if_y_allowed(curr_board,y) and self.check_diagonal_allowed(curr_board,x,y):
                    temp = curr_board[y]
                    temp_line = list(temp)
                    temp_line[x] = 'Q'
                    curr_board[y] = "".join(temp_line)
                    backtracking(x+1, curr_board)
                    curr_board[y] = temp

        backtracking(0,["." * n] * n)
        return res