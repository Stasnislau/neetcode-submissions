class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        latest_border = float('-inf')
        for inter in intervals:
            if inter[0] < latest_border:
                count += 1
            else:
                latest_border = inter[1]
        return count