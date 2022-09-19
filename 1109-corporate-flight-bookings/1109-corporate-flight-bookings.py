class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        for f, l, seats in bookings:
            res[f-1] += seats
            if l < n:
                res[l] -= seats
        for i in range(1, n):
            res[i] += res[i-1]
        return res