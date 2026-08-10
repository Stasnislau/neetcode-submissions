# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(one, two):
            if not one and not two:
                return None
            if one and two:
                one.val += two.val
                one.left = merge(one.left, two.left)
                one.right = merge(one.right, two.right)
                return one
            elif one:
                one.left = merge(one.left, None)
                one.right = merge(one.right, None)
                return one
            else:
                two.left = merge(None, two.left)
                two.right = merge(None, two.right)
                return two
        return merge(root1, root2)