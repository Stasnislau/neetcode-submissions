class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) -1 
        while left < right:
            dist = right - left
            currVal = dist * min(heights[left],heights[right])
            if currVal > maxArea:
                maxArea = currVal
            if heights[left] <= heights[right]:
                if dist == 1:
                    right -= 1
                    left += 1
                else:
                    left += 1
            else:
                right -= 1
        return maxArea

            



        