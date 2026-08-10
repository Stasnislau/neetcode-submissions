class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(startIndex, curr_nums):
            res.append(curr_nums.copy())
            if startIndex == len(nums):
                return
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue
                curr_nums.append(nums[i])
                backtrack(i+1, curr_nums)
                curr_nums.pop()
                
                
        backtrack(0, [])
        return res