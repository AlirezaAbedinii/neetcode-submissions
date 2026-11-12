"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]

        starts = sorted(starts)
        ends = sorted(ends)
        
        if not starts:
            return 0

        max_con = 1
        
        sp = 0
        ep = 0

        while sp < len(starts):
            if ends[ep] > starts[sp]:
                sp += 1
            else:
                max_con = max(max_con, sp-ep)
                ep += 1
        max_con = max(max_con, sp-ep)
        return max_con





        current = heapq.heappop(heap)

        