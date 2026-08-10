class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let l = 0;
        let max = 0;
        let maxFreq = 0;
        if (s.length <= k) {
            return s.length;
        }
        const map = new Map();
        for (let r = 0; r < s.length; r++) {
            map.set(s[r], (map.get(s[r]) || 0) + 1)
            maxFreq = Math.max(maxFreq, map.get(s[r]))
            while (r - l + 1 - maxFreq > k) {
                map.set(s[l], map.get(s[l]) - 1)
                l++;
            }
            max = Math.max(max, r - l + 1)
        }
        return max;
    }
}
