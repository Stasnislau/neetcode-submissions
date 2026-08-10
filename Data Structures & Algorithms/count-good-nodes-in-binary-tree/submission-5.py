# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:        
        return self.dfs(root)
    
    def dfs(self, node, max_val = float('-inf')):
        if not node:
            return 0
        res = 0
        if node.val >= max_val:
            max_val = node.val
            res += 1
        return res + self.dfs(node.left, max_val) + self.dfs(node.right, max_val)

        