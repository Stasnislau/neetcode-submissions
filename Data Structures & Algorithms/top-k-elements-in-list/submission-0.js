class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const map = new Map();
        for (let i = 0; i < nums.length; i++) {
            const item = map.get(nums[i]);
            if (!item) {
                map.set(nums[i], 1)
            }
            else {
                map.set(nums[i], item + 1)
            }
        }
        
        return [...map.entries()].sort((a, b) => b[1] - a[1]).slice(0, k).map(pair => {
            return pair[0]
        })
    }
}
