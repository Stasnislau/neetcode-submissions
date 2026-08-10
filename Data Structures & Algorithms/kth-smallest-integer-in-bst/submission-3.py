# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        valLeft = k
        while node:
            stack.append(node)
            node = node.left
        while k > 1:
            item = stack.pop()
            k -= 1
            if item.right:
                stack.append(item.right)
        return stack.pop().val
            

        