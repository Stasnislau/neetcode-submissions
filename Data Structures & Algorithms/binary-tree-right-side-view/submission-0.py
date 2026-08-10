# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], height: int) -> None:
            if not node:
                return;
            if len(arr) == height:
                arr.append(node.val)
            else:
                arr[height] = node.val;
            dfs(node.left, height + 1);
            dfs(node.right, height + 1)
            return
        arr = [];
        dfs(root, 0)
        return arr;