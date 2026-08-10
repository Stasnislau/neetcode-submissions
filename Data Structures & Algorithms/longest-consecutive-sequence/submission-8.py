class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        curr_count = 0
        for num in store:
            if num - 1 not in store:
                curr_count = 1
                while num + curr_count in store:
                    curr_count += 1
                res = max(res,curr_count)
        return res
