class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = {};
        for (let i = 0; i < nums.length; i++) {
            const num = nums[i];
            const trgt = target - num;
            if (trgt in map) {
                return [i, map[trgt]]
            }
            map[num] = i;
        }
    }
}
