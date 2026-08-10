class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const set = new Set();
        for (let i = 0; i < board.length; i += 3) {
            for (let j = 0; j < board.length; j += 3) {
                if (!this.checkSquares(board.slice(i, i + 3).map((item) =>
                    item.slice(j, j + 3))
                ))
                    return false
            }
        }

        for (let i = 0; i < board.length; i++) {
            set.clear();
            for (let j = 0; j < board[i].length; j++) {
                const item = board[i][j]
                if (item !== '.') {
                    if (set.has(item)) {
                        return false;
                    }
                    set.add(item);
                }
            }
            set.clear();
            for (let j = 0; j < board.length; j++) {
                const item = board[j][i]
                if (item !== '.') {
                    if (set.has(item)) {
                        return false;
                    }
                    set.add(item);
                }
            }
        }
        return true;
    }

    checkSquares(squar) {
        const set = new Set();
        for (let i = 0; i < squar.length; i++) {
            for (let j = 0; j < squar.length; j++) {
                if (squar[i][j] !== '.') {
                    if (set.has(squar[i][j])) {
                        return false;
                    }
                    set.add(squar[i][j]);
                }
            }
        }
        return true;
    }

}
