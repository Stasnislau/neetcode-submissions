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
        heap = []
        for inter in intervals:
            if heap and heap[0] <= inter.start:
                heapq.heappushpop(heap, inter.end)
            else:
                heapq.heappush(heap, inter.end)
        
        return len(heap)
            
        