class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const obj = {};

        if (strs.length < 2) {
            return [strs];
        }
        strs.forEach((str) => {
            const arr = new Array(26).fill(0);
            for (let i = 0; i < str.length; i++) {
                arr[str.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            }
            console.log(arr)
            const key = arr.join("-");
            console.log(key)
            if (!obj[key]) {
                obj[key] = [str];
            }
            else obj[key].push(str);
        })
        return Object.values(obj)
    }

}
