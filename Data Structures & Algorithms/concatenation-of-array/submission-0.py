class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        for i in range(len(nums)):
            res.append(nums[i])
        return res