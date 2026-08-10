from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)
        for x, row in enumerate(board):
            for y, tile in enumerate(row):
                if tile != '.':
                    if tile in rows[x] or tile in cols[y] or tile in squares[(x//3,y//3)]:
                        return False
                    rows[x].add(tile)
                    cols[y].add(tile)
                    squares[(x//3,y//3)].add(tile)
        return True


                    
                


        