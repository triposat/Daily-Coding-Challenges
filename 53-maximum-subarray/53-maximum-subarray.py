class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref = nums[:]
        suf=nums[:]
        for i in range(1, len(nums)):
            pref[i]+=max(0, pref[i-1])
        for i in range(len(nums)-2, -1, -1):
            suf[i]+=max(0, suf[i+1])
        def ans(arr, l, r):
            if l == r:
                return arr[l]
            mid = (l+r)//2
            return max(ans(arr, l, mid), ans(arr, mid+1, r), pref[mid]+suf[mid+1])
        return ans(nums, 0, len(nums)-1)