class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        def backtrack(curr_sum,i):
            if i == len(nums):
                return curr_sum
            return backtrack(curr_sum ^ nums[i], i+1) + backtrack(curr_sum, i + 1)
            
        return backtrack(0, 0)
            

            
            
