# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        visited = set()
        def dfs(node):
            if not node or node.val in visited:
                return
            res.append(node.val)
            visited.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

