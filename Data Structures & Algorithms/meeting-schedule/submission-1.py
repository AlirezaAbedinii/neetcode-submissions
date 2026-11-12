"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        int_list = [(interval.start, interval.end) for interval in intervals]
        heapq.heapify(int_list)
        if not intervals:
            return True
        prev = heapq.heappop(int_list)
        while int_list:
    
            current = heapq.heappop(int_list)
            if prev[1] > current[0]:
                return False
            
            prev = current
        
        return True