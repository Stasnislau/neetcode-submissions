# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root)
        return self.count
    
    def dfs(self, node, maxVal = float('-inf')):
        if not node:
            return
        if node.val >= maxVal:
            self.count += 1
            maxVal = node.val
        self.dfs(node.left, maxVal)
        self.dfs(node.right, maxVal)
        return

        