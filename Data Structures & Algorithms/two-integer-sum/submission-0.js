class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        for (let i = 0; i < nums.length - 1; i++) {
            let j = i + 1;
            while (j < nums.length) {
                if (nums[i] + nums[j] === target)
                    return [i, j]
                j++
            }
        }
    }
}
