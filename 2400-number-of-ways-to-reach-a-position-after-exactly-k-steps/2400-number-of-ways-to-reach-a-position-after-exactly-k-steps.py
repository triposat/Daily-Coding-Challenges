class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        n = k
        m = 10**9+7
        diff=abs(endPos-startPos)
        if diff>k:
            return 0
        r = (k-diff)//2
        res = 1
        if diff % 2 != k % 2:
            return 0
        return comb(n, r)%m