class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        const res = []
        function backtrack(open, close, string) {
            if (open === close && open === n) {
                res.push(string);
                return;
            }
            if (open < n) {
                backtrack(open + 1, close, string + '(');
            }
            if (open > close) {
                backtrack(open, close + 1, string + ')');
            }
        }
        backtrack(0, 0, "")
        return res;
    }
}
