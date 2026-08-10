# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float('-inf'),float('+inf'))
    def check(self, node, left, right):
        if not node:
            return True
        if node.val <= left or node.val >= right:
            return False
        leftVal = self.check(node.left, left, node.val)
        if not leftVal:
            return False
        rightVal = self.check(node.right, node.val, right)
        if not rightVal: 
            return False
        return leftVal and rightVal
        