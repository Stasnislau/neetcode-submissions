class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(j, curr_nums, visited):
            if j == len(nums):
                res.append(curr_nums.copy())
                return
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                curr_nums.append(nums[i])
                visited.add(nums[i])
                backtrack(j+1, curr_nums, visited)
                visited.remove(nums[i])
                curr_nums.pop()
        backtrack(0, [], set())
        return res
