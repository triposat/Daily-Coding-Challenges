class Solution:
    def minimumMoney(self, t: List[List[int]]) -> int:
        cost, cBack = [ele for ele in t if ele[0] > ele[1]], [
            ele for ele in t if ele[0] <= ele[1]]
        cost.sort(key=lambda x: x[1])
        cur = 0
        bud = 0
        for c, b in cost:
            cur -= c
            bud = min(bud, cur)
            cur += b
        if cBack:
            cur -= max(ele[0] for ele in cBack)
            bud = min(bud, cur)
        return abs(bud)
