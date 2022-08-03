class MyCalendar:

    def __init__(self):
        self.ans=[]

    def book(self, s1: int, e1: int) -> bool:
        for s0, e0 in self.ans:
            if not (s1>=e0 or e1<=s0):
                return False
        self.ans.append((s1, e1))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)