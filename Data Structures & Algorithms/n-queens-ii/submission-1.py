class Solution:
    def totalNQueens(self, n: int) -> int:
        taken_y = set()
        pos_diagonal = set()
        neg_diagonal = set()
        board = []
        self.total = 0
        def backtracking(x):
            if x == n:
                self.total += 1
            else:
                for y in range(n):
                    if y in taken_y or (x + y) in pos_diagonal or (x-y) in neg_diagonal:
                        continue
                    else:
                        pos_diagonal.add(x + y)
                        neg_diagonal.add(x - y)
                        taken_y.add(y)
                        backtracking(x+1)
                        pos_diagonal.remove(x+y)
                        neg_diagonal.remove(x - y)
                        taken_y.remove(y)
        backtracking(0)
        return self.total