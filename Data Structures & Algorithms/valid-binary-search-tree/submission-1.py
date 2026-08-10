# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], interval_low: int, interval_high ) -> bool:
            if not node:
                return True
            if node.val > interval_low and node.val < interval_high:
                return dfs(node.left, interval_low, node.val) and dfs(node.right, node.val,interval_high)
            else:
                return False
        return dfs(root, -1001, 1001)
                
            