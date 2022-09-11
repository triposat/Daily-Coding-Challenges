class Solution:
    def partitionString(self, s: str) -> int:
        ans = ""
        res = []
        for c in s:
            if c in ans:
                res.append(ans)
                ans = ""
                ans += c
            else:
                ans += c
        return len(res)+1