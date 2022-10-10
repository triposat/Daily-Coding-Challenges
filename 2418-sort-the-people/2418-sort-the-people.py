class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []
        for n, h in zip(names, heights):
            ans.append((-1*h, n))
        heapify(ans)
        res = []
        while ans:
            res.append(heappop(ans)[1])
        return res