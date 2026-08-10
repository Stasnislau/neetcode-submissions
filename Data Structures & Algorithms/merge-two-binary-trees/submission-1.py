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
            val1 = one.val if one else 0
            val2 = two.val if two else 0
            left1 = one.left if one else None
            left2 = two.left if two else None
            right1 = one.right if one else None
            right2 = two.right if two else None
            new_node = one if one else two
            new_node.val = val1 + val2
            new_node.left = merge(left1, left2)
            new_node.right = merge(right1, right2)
            return new_node
        return merge(root1, root2)