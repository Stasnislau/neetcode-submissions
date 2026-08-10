class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const set = new Set();
        for (let i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }
        let max = 0;
        for (let i = 0; i < nums.length; i++) {
            if (!set.has(nums[i] - 1)) {
                let j = 1;
                while (set.has(nums[i] + j)) {
                    j++;
                }
                if (j > max)
                    max = j
            }
        }
        return max;
    }
}
