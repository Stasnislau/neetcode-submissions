class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if (s1.length > s2.length) {
            return false;
        }
        const substr1 = new Array(26).fill(0);
        const substr2 = new Array(26).fill(0);
        for (let i = 0; i < s1.length; i++) {
            substr1[s1.charCodeAt(i) - 'a'.charCodeAt(0)]++;
        }
        const n = s1.length;
        let l = 0;
        for (let r = 0; r < s2.length; r++) {
            substr2[s2.charCodeAt(r) - 'a'.charCodeAt(0)]++;
            if (r - l + 1 === n) {
                if (substr1.every((value, index) => value === substr2[index]))
                    return true
                substr2[s2.charCodeAt(l) - 'a'.charCodeAt(0)]--;
                l++;
            }
        }
        return false;
    }
}
