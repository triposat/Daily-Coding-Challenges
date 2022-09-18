class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        res = 0
        for t0, t1, t2 in trips:
            while heap and heap[0][0] <= t1:
                res -= heappop(heap)[1]
            heappush(heap, (t2, t0))
            res += t0
            if res > capacity:
                return False
        return True