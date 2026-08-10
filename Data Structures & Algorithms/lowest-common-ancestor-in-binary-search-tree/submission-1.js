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
        const minNum = Math.min(p.val, q.val);
        const maxNum = Math.max(p.val, q.val)
        const res = new Map();
        function dfs(node) {
            if (node === null)
                return
            console.log(node.val, minNum, maxNum)
            if (node.val === maxNum) {
                res.set(node.val, node);
                return;
            }
            if (node.val > maxNum) {
                dfs(node.left);
            }
            else {
                if (node.val >= minNum) {
                    res.set(node.val, node);
                    return;
                } else {
                    dfs(node.right);
                }
            }
        }
        dfs(root);
        const answerKey = Math.min(...res.keys())
        return res.get(answerKey)
    }
}
