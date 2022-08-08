class Solution:
    def dfs(self, dp, nums, tar, res):
        if dp[tar] != -1:
            return dp[tar]
        res=0
        for ele in nums:
            if ele <= tar:
                res += self.dfs(dp, nums, tar-ele, res)
        dp[tar] = res
        return dp[tar]

    def combinationSum4(self, nums: List[int], tar: int) -> int:
        dp = [-1]*(tar+1)
        dp[0] = 1
        self.dfs(dp, nums, tar, 0)
        return dp[tar]