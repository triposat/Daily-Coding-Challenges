class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        count = 1
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]
        for inter in intervals[1:]:
            if inter[0] >= end:
                count += 1
                end = inter[1]
            else:
                end = min(end, inter[1])
        return n-count