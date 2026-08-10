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
            const row = board.map(item => {
                return item[i];
            })
            let shouldReturn = false;
            board[i].forEach(item => {
                if (item !== '.' && set.has(item)) {
                    shouldReturn = true;
                }
                else
                    set.add(item);
            })
            set.clear();
            row.forEach(item => {
                if (item !== '.' && set.has(item)) {
                    shouldReturn = true;
                }
                else
                    set.add(item);
            })
            set.clear();
            if (shouldReturn)
                return false;
        }
        return true;
    }

    checkSquares(squar) {
        const set = new Set();
        for (let i = 0; i < squar.length; i++) {
            for (let j = 0; j < squar.length; j++) {
                if (set.has(squar[i][j]) && squar[i][j] !== '.') {
                    return false;
                }
                set.add(squar[i][j])
            }
        }
        return true;
    }
}
