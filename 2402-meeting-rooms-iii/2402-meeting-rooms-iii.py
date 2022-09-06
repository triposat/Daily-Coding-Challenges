from heapq import *

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = list(range(0, n))
        ans = [0]*n
        meet = []
        heapify(meet)

        for s, e in sorted(meetings):
            while meet and meet[0][0] <= s:
                alr, r = heappop(meet)
                heappush(rooms, r)
            if rooms:
                r = heappop(rooms)
                heappush(meet, (e, r))
            else:
                alr, r = heappop(meet)
                heappush(meet, (alr+(e-s), r))
            ans[r] += 1
        return ans.index(max(ans))