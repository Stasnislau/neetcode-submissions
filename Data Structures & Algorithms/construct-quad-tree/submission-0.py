"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, n):
            is_same = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        is_same = False
                        break
            if is_same:
                return Node(grid[r][c], True)
            n = n // 2
            topL = dfs(r, c, n)
            topR = dfs(r, c + n, n)
            botL = dfs(r + n, c, n)
            botR = dfs(r + n, c + n, n)
            return Node(0, False, topL, topR, botL, botR)
        return dfs(0,0,len(grid))
