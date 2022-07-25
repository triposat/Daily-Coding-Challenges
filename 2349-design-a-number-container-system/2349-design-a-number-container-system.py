from sortedcontainers import SortedList
from collections import defaultdict


class NumberContainers:

    def __init__(self):
        self.first = defaultdict(SortedList)
        self.second = {}

    def change(self, index: int, number: int) -> None:
        if index in self.second:
            n = self.second[index]
            self.first[n].remove(index)
        self.second[index] = number
        self.first[number].add(index)

    def find(self, number: int) -> int:
        if number in self.first and self.first[number]:
            return self.first[number][0]
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
