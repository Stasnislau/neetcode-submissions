class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            mid = (l + r) // 2
            curr_weight = 0
            curr_days = 1
            i = 0
            for wg in weights:
                if curr_weight + wg > mid:
                    curr_days += 1
                    curr_weight = 0
                curr_weight += wg
                            

            
                
            if curr_days <= days:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res