import math
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        q = deque([0])
        visited = set()
        while q:
            curr_item = q.popleft()
            for i in range(len(nums)):
                if i in visited:
                    continue
                if math.gcd(nums[curr_item], nums[i]) > 1:
                    visited.add(i)
                    q.append(i)
        return len(visited) == len(nums)