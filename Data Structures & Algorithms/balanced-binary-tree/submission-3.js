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
     * @return {boolean}
     */
    isBalanced(root) {
        let isCorrect = true;
        function bal(node) {

            if (node === null) {
                return 0;
            }
            const left = bal(node.left);
            const right = bal(node.right);
            if (Math.abs(left - right) > 1) {
                isCorrect = false;
            }
            return Math.max(left, right) + 1
        }
        bal(root);
        return isCorrect;
    }


}
