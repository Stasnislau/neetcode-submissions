class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(curr_arr, checked ): 
            if len(curr_arr) == len(nums):
                res.append(curr_arr.copy())
                return
            for i in range(len(nums)):
                if i in checked:
                    continue
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in checked:
                    continue
                curr_arr.append(nums[i])
                checked.add(i)
                backtrack(curr_arr, checked)
                curr_arr.pop()
                checked.discard(i)
        backtrack([], set())
        return res

                
                
                
                 
            
