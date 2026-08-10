class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) -1 
        while left < right:
            dist = right - left
            currVal = dist * min(heights[left],heights[right])
            maxArea = max(currVal, maxArea)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea

            



        