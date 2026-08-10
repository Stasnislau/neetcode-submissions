class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        map = dict()

        for num in nums:
            if map.get(num):
                return True
            map[num] = 1;
        return False
        