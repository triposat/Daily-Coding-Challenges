from sortedcontainers import SortedList


class NumberContainers:

    def __init__(self):
        self.fir = defaultdict(SortedList)
        self.sec = {}

    def change(self, ind: int, number: int) -> None:
        if ind in self.sec:
            n = self.sec[ind]
            self.fir[n].remove(ind)
        self.sec[ind] = number
        self.fir[number].add(ind)

    def find(self, number: int) -> int:
        if number in self.fir:
            if self.fir[number]:
                return self.fir[number][0]
        return -1