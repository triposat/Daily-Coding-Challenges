class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref=0
        suf=0
        maxi=-float("inf")
        for i in range(len(nums)):
            pref=nums[i]*(pref or 1)
            suf=nums[~i]*(suf or 1)
            maxi=max(maxi, pref, suf)
        return maxi