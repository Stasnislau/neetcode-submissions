from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checked = set(nums)
        longestOverall = 0
        longestCurrent = 0

        for num in checked:
            longestCurrent = 1
            if num-1 not in checked:
                currentNum = num
                while currentNum + 1 in checked:
                    longestCurrent += 1
                    currentNum += 1
            longestOverall = max(longestCurrent, longestOverall)
        return longestOverall