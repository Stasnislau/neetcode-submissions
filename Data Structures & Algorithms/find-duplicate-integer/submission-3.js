class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findDuplicate(nums) {
        console.log(nums)
        for (let i = 0; i < nums.length; i++) {
            const index = Math.abs(nums[i]) - 1;
            console.log(nums[index], nums[i])
            if (nums[index] < 0)
                return Math.abs(nums[i])
            else
            {
                nums[index] *= -1;
            }
        }
        console.log(nums)
    }
}
