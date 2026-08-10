class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1;
        postfix = 1;

        for i in range(1, len(nums)):
            prefix = prefix * nums[i-1]
            result[i] = prefix

        for i in range(len(nums) - 2, -1, -1):
            postfix = postfix * nums[i + 1]
            result[i] = result[i] * postfix

        # for i in range(len(nums)):
        #     result [i] = right[i] * left[i]
        # print(left, right)
        return result

