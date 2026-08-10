class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        taken_y = set()
        pos_diagonal = set()
        neg_diagonal = set()
        board = []
        res = []
        def backtracking(x):
            if x == n:
                cur_board = ["".join("Q" if col == y else '.' for col in range(n) ) for y in board]
                res.append(cur_board)
                return
            for y in range(n):
                if y in taken_y or (y + x) in pos_diagonal or (y - x) in neg_diagonal:
                    continue
                taken_y.add(y)
                pos_diagonal.add(y + x)
                neg_diagonal.add(y - x)
                board.append(y)
                backtracking(x+1)
                board.pop()
                taken_y.remove(y)
                pos_diagonal.remove(y + x)
                neg_diagonal.remove(y - x)

        backtracking(0)
        print(res)
        return res