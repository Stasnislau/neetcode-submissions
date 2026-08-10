class Solution:
    def totalNQueens(self, n: int) -> int:
        taken_y = set()
        pos_diagonal = set()
        neg_diagonal = set()
        board = []
        self.total = 0
        def backtracking(x):
            if x == n:
                cur_board = ["".join("Q" if col == y else '.' for col in range(n) ) for y in board]
                self.total += 1
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
        return self.total