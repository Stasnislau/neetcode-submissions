class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        postfix = 1;

        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            postfix = postfix * nums[i + 1]
            result[i] = result[i] * postfix

        return result

