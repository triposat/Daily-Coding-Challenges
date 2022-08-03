class MyCalendar:

    def __init__(self):
        self.ans = []

    def book(self, start: int, end: int) -> bool:
        ans = self.ans
        idx = bisect_left(ans, (start, end))
        left_valid = idx == 0 or ans[idx-1][1] <= start
        right_valid = idx == len(ans) or ans[idx][0] >= end
        if left_valid and right_valid:
            ans.insert(idx, (start, end))
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
