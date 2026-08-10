class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 1):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    curr_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if curr_sum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                        while nums[r] == nums[r+1] and l < r:
                            r -= 1
                    elif curr_sum > target:
                        r -= 1
                    else:
                        l += 1

                        
        return res
