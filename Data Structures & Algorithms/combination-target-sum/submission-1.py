class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr_nums, curr_sum):
            if curr_sum == target:
                res.append(curr_nums.copy())
                return
            if curr_sum > target or i >= len(nums):
                return
            curr_nums.append(nums[i])
            curr_sum += nums[i]
            dfs(i, curr_nums, curr_sum)
            
            curr_nums.pop()
            curr_sum -= nums[i]
            dfs(i + 1, curr_nums, curr_sum)
        dfs(0, [], 0)
        return res
