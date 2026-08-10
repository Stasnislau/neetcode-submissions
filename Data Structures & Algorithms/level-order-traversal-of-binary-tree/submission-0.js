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
     * @return {number[][]}
     */
    levelOrder(root) {
        const map = new Map();

        function dfs(node, level) {
            if (node === null)
                return;
            map.set(level, [...(map.get(level) || []), node.val])
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        }
        dfs(root, 0);
        console.log(map)

        return Array.from(map.values());
    }
}
