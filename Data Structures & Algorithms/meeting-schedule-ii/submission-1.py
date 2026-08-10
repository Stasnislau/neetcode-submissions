"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
            
        intervals.sort(key = lambda x: x.start)
        max_durs = []
        def checkIfIntersects(interval):
            for ind, dur in enumerate(max_durs):
                if interval.start >= dur:
                    return ind
            return -1


        for i in range(len(intervals)):
            intersects_index = checkIfIntersects(intervals[i])
            if intersects_index != -1:
                max_durs[intersects_index] = max(max_durs[intersects_index], intervals[i].end)
            else:
                max_durs.append(intervals[i].end)
                
        return len(max_durs)
            
        