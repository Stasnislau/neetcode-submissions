class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0;
        let r = nums.length - 1;
        while (l <= r) {
            const middle = Math.floor((l + r) / 2);
            console.log(middle)
            if (nums[middle] === target)
                return middle;
            else if (nums[middle] > target) {
                r = middle - 1;
            }
            else {
                l = middle + 1;
            }
        }
        return -1;
    }
}
