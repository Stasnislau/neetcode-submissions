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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    lowestCommonAncestor(root, p, q) {
        const min = Math.min(p.val, q.val);
        const max = Math.max(p.val, q.val)
        let cur = root;
        while (cur) {
            if (cur.val === max || cur.val === min) {
                return cur;
            }
            if (cur.val < max && cur.val > min) {
                return cur;
            }
            if (cur.val > max)
                cur = cur.left;
            else
                cur = cur.right
        }
    }
}
