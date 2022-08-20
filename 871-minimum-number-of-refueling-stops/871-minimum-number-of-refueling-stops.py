class Solution:
    def minRefuelStops(self, target: int, st: int, arr: List[List[int]]) -> int:
        dis = st
        i = 0
        maxHp = []
        heapify(maxHp)
        n = len(arr)
        stops = 0
        while dis < target:
            while i < n and arr[i][0] <= dis:
                heappush(maxHp, -1*arr[i][1])
                i += 1
            if not maxHp:
                return -1
            dis += -1*heappop(maxHp)
            stops += 1
        return stops