class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const map = new Map();
        let max = 0;
        let l = 0;
        let currLength = 0;
        for (let r = 0; r < s.length; r++) {
            console.log(map)
            while (map.get(s[r]) && r > l) {
                console.log(map, "DELETE")
                map.delete(s[l]);
                l++;
            }
            map.set(s[r], 1)
            currLength = r - l + 1;
            console.log("CURRENT LENGTH", currLength)
            if (max < currLength)
                max = currLength;
        }
        return max;
    }
}
