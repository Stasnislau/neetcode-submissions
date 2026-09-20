class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[0]
        for i in range(1, len(triangle)):
            new = triangle[i]
            new[0] += prev[0]
            for j in range(1, len(new) - 1):
                new[j] += min(prev[j], prev[j-1])
            new[-1] += prev[-1]
            prev = new
        return min(prev)