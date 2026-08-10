# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, l, r):
            if not node:
                return TreeNode(val)
            if l < val < r:
                if node.val < val:
                    node.right = dfs(node.right, node.val, r)
                    return node
                else:
                    node.left = dfs(node.left, l, node.val)
                    return node
            return None

        l = float('-inf')
        r = float('inf')
        return dfs(root,l,r) 

