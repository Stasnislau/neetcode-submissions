class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2
            curr_sum = 0
            curr_i = 1
            for num in nums:
                if curr_sum + num <= mid:
                    curr_sum += num
                else:
                    curr_sum = num
                    curr_i += 1          
            if curr_i <= k:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res