class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]
        result = [1 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            if i == 0:
                left[i] = num;
            else:
                left[i] = left[i - 1] * num

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if i == len(nums) - 1:
                right[i] = num;
            else:
                right[i] = right[i + 1] * num

        for i, num in enumerate(nums):
            if i == len(nums) -1:
                result[i] = left[i - 1]
            elif i == 0:
                result[i] = right[i + 1]
            else:
                result [i] = right[i + 1] * left[i-1]
        print(left, right)
        return result

