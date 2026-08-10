class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for index, fixedNum in enumerate(nums):
            if index != 0 and nums[index - 1] == fixedNum:
                continue;
            left = index + 1
            right = len(nums) - 1

            while left < right:
                print(res)
                sum = fixedNum + nums[left] + nums[right]
                if sum == 0:
                    res.append([fixedNum,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return res


