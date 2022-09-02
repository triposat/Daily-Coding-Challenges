class Solution:
    def maxProfit(self, p: List[int]) -> int:
        ans = 0
        res = 0
        for i in range(1, len(p)):
            ans += p[i]-p[i-1]
            if ans < 0:
                ans = 0
            res = max(res, ans)
        return res