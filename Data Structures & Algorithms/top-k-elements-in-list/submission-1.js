class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const map = new Map();
        const buckets = [];
        const result = [];
        for (let i = 0; i < nums.length; i++) {
            const num = nums[i]
            map.set(num, (map.get(num) || 0) + 1)
        }

        for (let [num, freq] of map) {
            buckets[freq] = buckets[freq] || [];
            buckets[freq].push(num);
        }
        console.log(buckets)
        for (let i = buckets.length-1; i > 0 && result.length < k; i--) {
            if (buckets[i]){
                result.push(...buckets[i])
            }
        }
        return result;
    }
}
