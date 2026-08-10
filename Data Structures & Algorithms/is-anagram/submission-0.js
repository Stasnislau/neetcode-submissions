class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length)
            return false;
        const sSet = new Map();
        const tSet = new Map();
        for (let sym of s) {
            const value = sSet.get(sym);
            if (value) {
                sSet.set(sym, value + 1)
            }
            else
                sSet.set(sym, 1)
        }
        for (let sym of t) {
            const value = tSet.get(sym);
            if (value) {
                tSet.set(sym, value + 1)
            }
            else
                tSet.set(sym, 1)
        }
        const keys = Array.from(sSet.keys());
        console.log(keys)
        for (let value of keys) {
            console.log(value)
            if (sSet.get(value) !== tSet.get(value))
                return false;
        }
        return true;
    }
}
