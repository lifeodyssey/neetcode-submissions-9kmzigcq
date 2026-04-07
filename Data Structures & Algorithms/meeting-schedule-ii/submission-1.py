"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals=sorted(intervals,key=lambda x:x.start)
        heap=[]
        maxRooms=0
        for interval in intervals:
            if heap and interval.start>=heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,interval.end)
            maxRooms=max(maxRooms,len(heap))
            
        return maxRooms