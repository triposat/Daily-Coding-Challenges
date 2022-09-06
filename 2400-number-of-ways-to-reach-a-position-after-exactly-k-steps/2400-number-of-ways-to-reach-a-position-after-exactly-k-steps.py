class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        diff = abs(endPos-startPos)
        m = 10**9+7

        n = k
        r = (k-diff)//2

        if diff % 2 != k % 2 or diff > k:
            return 0
        return comb(n, r) % m