class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        total = sum(nums)
        if total % k != 0 or len(nums) < k:
            return False
        target = total // k
        if max(nums) > target:
            return False

        def backtrack(i, curr_arr):
            if i == len(nums):
                return all(el == 0 for el in curr_arr)
                       
            for j in range(k):
                if j > 0 and curr_arr[j] == curr_arr[j-1]:
                    continue
                if curr_arr[j] - nums[i] >= 0:
                    curr_arr[j] -= nums[i]
                    if backtrack(i+1, curr_arr):
                        return True
                    curr_arr[j] += nums[i]
            return False
        return backtrack(0, [target] * k)  