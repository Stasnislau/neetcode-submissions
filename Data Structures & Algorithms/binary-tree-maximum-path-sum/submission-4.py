# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxVal = float('-inf')
        self.dfs(root)
        return self.maxVal

    def dfs(self, node):
        if not node:
            return float('-inf')
        leftVal = self.dfs(node.left)
        rightVal = self.dfs(node.right)
        bestChild = max( node.val, leftVal + node.val, rightVal + node.val)
        maxValue = max(bestChild,leftVal, rightVal, rightVal + leftVal + node.val)
        self.maxVal = max(maxValue, self.maxVal)
        print(maxValue, bestChild, node.val)
        return bestChild