from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(lambda: defaultdict(int))
        rows = defaultdict(lambda: defaultdict(int))
        cols = defaultdict(lambda: defaultdict(int))
        for x, row in enumerate(board):
            for y, tile in enumerate(row):
                if tile != '.':
                    if rows[f'{x}'][tile] != 0 or cols[f'{y}'][tile] != 0 or squares[f'{x//3}{y//3}'][tile] != 0:
                        return False
                    rows[f'{x}'][tile] = 1
                    cols[f'{y}'][tile] = 1
                    squares[f'{x//3}{y//3}'][tile] = 1
        return True


                    
                


        