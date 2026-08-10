# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    largest = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.largest
    
    def dfs(self, root):
        if not root:
            return 0
        width = self.dfs(root.left) + self.dfs(root.right)
        depth = 1 + max(self.dfs(root.left), self.dfs(root.right))
        self.largest = max(self.largest, width)
        return depth
    
