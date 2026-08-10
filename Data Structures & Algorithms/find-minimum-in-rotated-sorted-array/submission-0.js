class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let l = 0;
        let r = nums.length - 1;
        while (l < r) {
            const middle = Math.floor((l + r) / 2)
            console.log(l, r , middle)
            if (nums[middle] > nums[r]) {
                l = middle + 1;
            }
            else
                r = middle;
        }
        return nums[l]
    }
}
