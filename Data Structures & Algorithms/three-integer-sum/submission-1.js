class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a, b) => a - b);
        const result = [];
        console.log(nums)
        for (let i = 0; i < nums.length - 1; i++) {
            const target = -nums[i];
            if (i > 0 && nums[i] === nums[i-1])
                continue;
            let begin = i + 1;
            let end = nums.length - 1;
            
            while (begin < end) {
                if (nums[begin] + nums[end] === target) {
                    result.push([nums[begin], nums[i], nums[end]])
                    begin++;
                    end--;
                    while (begin < end && nums[begin] === nums[begin - 1]) {
                        begin++;
                    }
                }
                else if (nums[begin] + nums[end] > target)
                    end--;
                else
                    begin++;
            }
        }
        return result;
    }
}
