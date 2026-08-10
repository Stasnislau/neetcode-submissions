class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length)
            return false;
        const map = new Array(26).fill(0);
        for (let i = 0; i < s.length; i++) {
            console.log(s[i].charAt() - 'a'.charAt())
            map[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            map[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
        }

        return map.every(item => item === 0)
    }
}
