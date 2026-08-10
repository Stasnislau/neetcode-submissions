class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        let l = 0;
        let r = matrix.length * matrix[0].length - 1;
        while (l <= r) {
            const middle = Math.floor((l + r) / 2)
            const i = Math.floor(middle / matrix[0].length)
            const j = middle % matrix[0].length;
            console.log(middle, i, j, l, r, matrix[i][j], target)
            const item = matrix[i][j];
            if (item === target) {
                return true;
            }
            else if (item > target) {
                r = middle - 1;
            }
            else {
                l = middle + 1;
            }
        }
        return false;
    }
}
