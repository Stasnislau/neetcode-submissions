# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        if not root:
            return []
        q = deque([root])
        node = root
        while q:
            currLevel = []
            for _ in range (len(q)):
                item = q.popleft()
                if item.left: q.append(item.left)
                if item.right: q.append(item.right)
                currLevel.append(item.val)
            arr.append(currLevel[-1])
            

        return arr