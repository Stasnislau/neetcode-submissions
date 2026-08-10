class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        i = 0
        j = 0
        checked = set()
        while j < len(nums):
            if nums[j] in checked:
                print(j, i)
                return True
            else:
                checked.add(nums[j])
            if j - i < k:
                j += 1
            else:
                checked.remove(nums[i])
                i += 1
                j += 1

        return False
                


