class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        e.sort(key=lambda x: (x[0], -x[1]))
        res = []
        for w, h in e:
            idx = bisect.bisect_left(res, h)
            if idx == len(res):
                res.append(h)
            else:
                res[idx] = h
        return len(res)