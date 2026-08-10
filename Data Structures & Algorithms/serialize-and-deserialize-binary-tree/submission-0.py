# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:

    
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        q = deque([root])
        s = []
        while q:
            item = q.popleft()
            if item == None:
                s.append('-')
            else:
                s.append(f'{item.val}')
                if item.left: 
                    q.append(item.left) 
                else: 
                    q.append(None)
                if item.right: 
                    q.append(item.right) 
                else: 
                    q.append(None)
        return "#".join(s)



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '':
            return None
        nodes = data.split('#')
        
        currLevel = 1
        root = TreeNode(nodes[0])
        q = deque([root])
        print(nodes, len(nodes))
        j = 1
        while q or j < len(nodes):
            if not q:
                return
            item = q.popleft()
            print(q, j)
            if nodes[j] == '-':
                item.left = None
            else:
                item.left = TreeNode(int(nodes[j]))
                q.append(item.left)
            j += 1
            if nodes[j] == '-':
                item.right = None
            else:
                item.right = TreeNode(int(nodes[j]))
                q.append(item.right)
            j += 1
            

            
            



        return root

            

