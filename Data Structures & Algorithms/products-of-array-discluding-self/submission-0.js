class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let totalProduct = 1;
        let zeroDetected = false;
        nums.forEach((item) => {
            if (item !== 0 || zeroDetected) {
                totalProduct *= item
            }
            else zeroDetected = true;
        })
        if (totalProduct === 0) {
            return nums.map(() => 0)
        }
        return nums.reduce((result, item) => {
            if (item === 0) {
                result.push(totalProduct);
            }
            else if (zeroDetected) {
                result.push(0)
            } else
                result.push(totalProduct / item)
            return result;
        }, []);
    }
}
