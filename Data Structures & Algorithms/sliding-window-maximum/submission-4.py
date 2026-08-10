from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = 0

        for r in range(len(nums)):
            if not q or nums[q[0]] <= nums[r]:
                q.clear()
                q.append(r)
            elif nums[q[0]] > nums[r]:
                while nums[q[-1]] < nums[r]:
                    q.pop()
                q.append(r)
            if r - l + 1 == k:
                if q[0] < r - k + 1:
                    q.popleft()
                res.append(nums[q[0]])
                l += 1
        return res

            