class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, num in enumerate(nums): 
            diff = target - num
            if diff in checked:
                return [checked[diff], i];
            checked[num] = i
        return []