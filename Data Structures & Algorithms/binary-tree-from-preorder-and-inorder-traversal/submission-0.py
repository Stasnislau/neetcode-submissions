# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        rootVal = preorder[0]
        rootIndexInorder = inorder.index(rootVal)
        inorderLeft = inorder[:rootIndexInorder]
        inorderRight = inorder[rootIndexInorder + 1:]
        print(inorderLeft, inorderRight, rootVal)
        rootNode = TreeNode(rootVal)
        rootNode.left = self.buildTree(preorder[1:len(inorderLeft) + 1], inorderLeft)
        rootNode.right = self.buildTree(preorder[len(inorderLeft) + 1:], inorderRight)
        return rootNode
        


            





        