from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = defaultdict(lambda: False)
        self.found = False
        x_max = len(board[0])
        y_max = len(board)
        def backtrack(x,y, j):
            if j == len(word) or self.found:
                return
            if word[j] != board[y][x] or self.visited[f'{x}-{y}']:
                print('visited kurwa', x,y)
                return
            self.visited[f'{x}-{y}'] = True
            print(j, board[y][x] )
            if x + 1 < x_max:
                backtrack(x + 1, y, j+1)
            if x > 0:
                backtrack(x - 1, y, j+1)
            if y > 0:
                backtrack(x, y - 1, j+1)
            if y + 1 < y_max:
                backtrack(x, y + 1, j+1)
            self.visited[f'{x}-{y}'] = False
            if j == len(word) - 1:
                print('updating found')
                self.found = True
                return 

            
        for y in range(y_max):
            for x in range(x_max):
                    self.visited = defaultdict(bool)
                    print(self.visited, x,y)
                    backtrack(x,y, 0)
                    if self.found:
                        return True
        return False