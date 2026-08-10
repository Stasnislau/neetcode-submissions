class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(j, curr_nums):
            if j == len(nums):
                res.append(curr_nums.copy())
                return
            for i in range(len(nums)):
                if nums[i] in curr_nums:
                    continue
                curr_nums.append(nums[i])
                backtrack(j+1, curr_nums)
                curr_nums.pop()
        backtrack(0, [])
        return res
