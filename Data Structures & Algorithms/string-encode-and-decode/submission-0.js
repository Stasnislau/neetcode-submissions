class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        return strs.reduce((result, str) => {
            return result = result + str.length + '#' + str;
        }, "")
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const result = [];
        console.log(str)
        let endIndex = 0;
        for (let i = 0; i < str.length; i++) {
            if (str[i] === "#") {
                const length = parseInt(str.slice(endIndex, i));
                endIndex = i + length + 1;
                console.log(str.slice(i + 1, endIndex))
                result.push(str.slice(i + 1, endIndex));
                i += length;
            }
        }
        return result;
    }
}
