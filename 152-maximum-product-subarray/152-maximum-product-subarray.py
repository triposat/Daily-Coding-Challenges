class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref=nums[:]
        suf=nums[:]
        for i in range(1, len(nums)):
            pref[i]*=pref[i-1] or 1
        for i in range(len(nums)-2, -1, -1):
            suf[i]*=suf[i+1] or 1
        return max(pref+suf)