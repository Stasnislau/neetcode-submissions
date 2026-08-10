class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = sum(nums)
        sums = [nums_sum]
        count = 1 if nums_sum == target else 0
        for num in nums:
            new_sums = sums.copy()
            for el in new_sums:
                curr_sum = el - num * 2
                if curr_sum == target:
                    count += 1
                sums.append(curr_sum)
        return count


            



