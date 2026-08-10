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
     * @return {number}
     */
    diameterOfBinaryTree(root) {

        if (root === null) {
            return 0;
        }
        let result = 0;
        function calc(node) {
            if (node === null) {
                return 0;
            }
            const left = calc(node.left);
            const right = calc(node.right);
            console.log(left, right)
            result = Math.max(left + right, result)
            return Math.max(left, right) + 1;
        }
        calc(root, 0);

        return result
    }


}
