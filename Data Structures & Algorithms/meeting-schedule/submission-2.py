"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        current_end = float('-inf')
        for inter in intervals:
            if inter.start < current_end:
                return False
            else:
                current_end = inter.end
        return True
