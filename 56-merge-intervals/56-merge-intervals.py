class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        oldInter = intervals[0]
        res = [oldInter]
        for inter in intervals[1:]:
            if inter[0] <= oldInter[1]:
                oldInter[1] = max(oldInter[1], inter[1])
            else:
                oldInter = inter
                res.append(oldInter)
        return res