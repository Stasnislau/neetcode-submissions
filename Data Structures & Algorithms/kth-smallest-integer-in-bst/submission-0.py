# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        
        def in_order(node):
            if not node or self.result is not None:
                return
            in_order(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            in_order(node.right)

        in_order(root)
        return self.result

            