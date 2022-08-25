class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo={}
        def ans(i):
            if i==len(nums)-1:
                memo[i]=nums[i]
                return nums[i]
            if i in memo:
                return memo[i]
            res = max(nums[i], nums[i]+ans(i+1))
            memo[i]=res
            return res
        ans(0)
        return max(memo.values())