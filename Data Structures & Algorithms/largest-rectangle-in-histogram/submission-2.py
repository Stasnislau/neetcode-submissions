class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = [] # height, index
        heights.append(0) # adding o to finish all the calculations at the end

        for i in range(len(heights)):
            storedIndex = i
            while stack and stack[-1][0] > heights[i]:
                popped = stack.pop()
                largest = max(largest, (i - popped[1]) * popped[0])
                storedIndex = popped[1]
            if heights[i] != 0:
                stack.append((heights[i], storedIndex))            
        
        return largest