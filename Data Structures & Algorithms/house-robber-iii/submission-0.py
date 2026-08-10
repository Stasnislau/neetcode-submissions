# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from functools import cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(root):
            if not root:
                return 0
            opt1 = root.val
            if root.left:
                opt1 += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                opt1 += dfs(root.right.left) + dfs(root.right.right)
            opt2 = dfs(root.left) + dfs(root.right)
            return max(opt1, opt2)
        return dfs(root)