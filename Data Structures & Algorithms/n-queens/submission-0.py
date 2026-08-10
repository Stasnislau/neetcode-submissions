def check_if_y_allowed(curr_board, y):
    return not 'Q' in curr_board[y]
def check_diagonal_allowed(curr_board, x,y):
    y1, y2 = y,y
    while x >= 0:
        if y1 >= 0:
            if curr_board[y1][x] == 'Q':
                return False
        if y2 < len(curr_board):
            if curr_board[y2][x] == 'Q':
                return False
        x -= 1;
        y1 -= 1
        y2 += 1
    return True
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtracking(x, y, curr_board):
            if y == n:
                return
            if x == n:
                res.append(curr_board[:])
                return
            if check_if_y_allowed(curr_board,y) and check_diagonal_allowed(curr_board,x,y):
                temp = curr_board[y]
                temp_line = list(temp)
                temp_line[x] = 'Q'
                curr_board[y] = "".join(temp_line)
                backtracking(x+1, 0, curr_board)
                curr_board[y] = temp
            backtracking(x, y+1, curr_board) 

        backtracking(0,0,["." * n] * n)
        return res