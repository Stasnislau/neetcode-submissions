"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.end)
        current_end = float('-inf')
        for interval in intervals:
            print(interval.start, interval.end ) 
        for inter in intervals:
            if inter.end < current_end or inter.start < current_end:
                return False
            else:
                current_end = inter.end
        return True
