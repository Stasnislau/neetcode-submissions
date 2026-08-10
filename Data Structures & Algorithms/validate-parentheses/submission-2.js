class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = [];
        for (let i = 0; i < s.length; i++) {
            if (s[i] === '(' || s[i] === '{' || s[i] === '[') {
                stack.push(s[i]);
            }
            else {
                const stackChar = stack.pop();
                if (!stackChar)
                    return false;
                if (stackChar.charCodeAt(0) + 1 !== s[i].charCodeAt(0)  && stackChar.charCodeAt(0)  + 2 !== s[i].charCodeAt(0))
                    return false;
            }
        }
        return stack.length === 0 ? true : false;
    }
}
