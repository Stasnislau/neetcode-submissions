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
    maxDepth(root) {
        if (root === null)
            return 0;
        return Math.max(this.dfs(root.left, 2), this.dfs(root.right, 2))
    }

    dfs(node, currMax) {
        if (node === null)
            return currMax - 1;
        return Math.max(this.dfs(node.left, currMax + 1), this.dfs(node.right, currMax + 1))
    }
}
