class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x_max = len(board[0])
        y_max = len(board)
        def backtrack(x,y, j):
            if j == len(word):
                return True
            if x < 0 or x >= x_max or y < 0 or y >= y_max:
                return False
            if word[j] != board[y][x]:
                return False
            temp = board[y][x]
            board[y][x] = '#'
            found = backtrack(x + 1, y, j+1) or backtrack(x - 1, y, j+1) or backtrack(x, y - 1, j+1) or backtrack(x, y + 1, j+1)
            board[y][x] = temp

            return found

            
        for y in range(y_max):
            for x in range(x_max):
                    if board[y][x] == word[0] and backtrack(x,y, 0):
                        return True
        return False