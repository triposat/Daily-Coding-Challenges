class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def ans(arr, l, r):
            if l > r:
                return -inf
            mid = (l+r)//2
            leftSum = 0
            rightSum = 0
            curSum = 0
            for i in range(mid-1, l-1, -1):
                leftSum = max(leftSum, curSum := curSum+arr[i])
            curSum = 0
            for j in range(mid+1, r+1):
                rightSum = max(rightSum, curSum := curSum+arr[j])
            print(leftSum, rightSum)
            return max(ans(arr, l, mid-1), ans(arr, mid+1, r), leftSum+arr[mid]+rightSum)
        return ans(nums, 0, len(nums)-1)