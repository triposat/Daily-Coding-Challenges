class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        add=0
        ans=-float("inf")
        for ele in nums:
            add+=ele
            ans=max(ans, add)
            if add<0:
                add=0
        return ans