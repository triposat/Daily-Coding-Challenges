class Solution:
    def maximumRobots(self, charge: List[int], cost: List[int], budget: int) -> int:
        res, add, start, mxheap = 0, 0, 0, []
        heapify(mxheap)
        for end in range(len(charge)):
            add += cost[end]
            heappush(mxheap, (-1*charge[end], end))
            while mxheap and -1*mxheap[0][0]+(end-start+1)*add > budget:
                add -= cost[start]
                while mxheap and mxheap[0][1] <= start:
                    heappop(mxheap)
                start += 1
            res = max(res, end-start+1)
        return res