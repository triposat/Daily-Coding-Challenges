class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref = nums[:]
        suf=nums[:]
        for i in range(1, len(nums)):
            pref[i]+=max(0, pref[i-1])
        return max(pref)