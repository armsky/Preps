"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Have you met this question in a real interview?
Example
Given intervals = [(0,30),(5,10),(15,20)], return 2.
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        res = 0
        meetings = []
        for i in intervals:
            meetings.append((i.start, 1))
            meetings.append((i.end, -1))

        meetings.sort()
        max_room = 0
        for t, cnt in meetings:
            res += cnt
            max_room = max(res, max_room)
        return max_room
