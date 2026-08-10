/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    isSubtree(root, subRoot) {
        function isSubtree(node, subNode) {
            if (!subNode)
                return true;
            if (!node)
                return false;
            if (isSameTree(node, subNode)) {
                return true;
            }
            return isSubtree(node.left, subRoot) || isSubtree(node.right, subRoot)

        }
        function isSameTree(node, subNode) {
            if (!node && !subNode) {
                return true
            }
            if (node && subNode && node.val === subNode.val) {
                return isSameTree(node.left, subNode.left) && isSameTree(node.right, subNode.right)
            }
            return false
        }
        return isSubtree(root, subRoot)
    }
}
