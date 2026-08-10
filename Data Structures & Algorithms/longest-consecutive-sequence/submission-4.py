from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checked = set(nums)

        starters = defaultdict(int)

        for num in checked:
            if num-1 not in checked:
                starters[num] = 1;

        for starter in starters: 
            num = starter
            while num + 1 in checked:
                starters[starter] += 1
                num += 1
        print (starters)
        if len(starters.values()) == 0:
            return 0
        return max(starters.values())
