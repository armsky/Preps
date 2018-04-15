"""
There is a process sequence that contains the start and end of each process.
There is a query sequence asking how many processes are running at a certain
point in time. Please return the query result of the query sequence.

 Notice
1 <= logs[i].start,logs[i].end,queries[i] <= 2^32 - 1
1 <= |logs|,|queries| <= 10^5
Have you met this question in a real interview?
Example
Given logs = [[1, 1234], [2, 1234]], queries = [2], return [2].

Explanation:
There are 2 processes running at time 2.
Given logs = [[1, 1234], [2, 1234]], queries = [1, 1235], return [1, 0].

Explanation:
There is a process running at time 1, and 0 processes running at time 1235.
"""
from collections import Counter
class Solution:
    """
    @param logs: Sequence of processes
    @param queries: Sequence of queries
    @return: Return the number of processes
    """
    def numberOfProcesses(self, logs, queries):
        def numberOfProcesses(self, logs, queries):
        map = Counter()
        times = set()
        for log in logs:
            times.add(log.start)
            map[log.start] += 1
            times.add(log.end)
            map[log.end] -= 1
        for q in queries:
            times.add(q)

        times = sorted(list(times))
        live = 0
        for t in times:
            if t in map:
                live += map[t]
                map[t] = live
            else:
                map[t] = live

        return [map[q] for q in queries]
