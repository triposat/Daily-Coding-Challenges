class Solution:
    def numTilings(self, n: int) -> int:
        dp=[1, 2, 5]
        # i=n-1
        for i in range(3, n):
            dp.append(2*dp[i-1]+dp[i-3])
        return dp[n-1]%(10**9+7)