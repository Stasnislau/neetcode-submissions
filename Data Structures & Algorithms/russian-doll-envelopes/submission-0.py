class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [h for _, h in envelopes]
        dp = []
        for h in heights:
            if not dp or dp[-1] < h:
                dp.append(h)
            else:
                l = 0
                r = len(dp) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if dp[mid] < h:
                        l = mid + 1
                    else:
                        r = mid - 1
                dp[l] = h
        return len(dp)