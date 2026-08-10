# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root, 0)
    def dfs(self,root, num):
        if not root:
            return num
        return max(self.dfs(root.left, num + 1), self.dfs(root.right, num + 1))
        
        