class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1;

        center = int((r + l) / 2)

        while l <= r:
            center = int((r + l) / 2)

            if nums[center] == target:
                return center
            elif nums[center] > target:
                r = center - 1
            else:
                l = center + 1
        return -1 




        