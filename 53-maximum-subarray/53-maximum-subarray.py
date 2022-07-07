# Brute Force Approach
# Time: O(n^2), Space: O(1)
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans = -float('inf')
#         for i in range(n):
#             curSum = 0
#             for j in range(i, n):
#                 curSum += nums[j]
#                 ans = max(ans, curSum)
#         return ans

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float('inf')
        curSum = 0
        for num in nums:
            curSum += num
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0
        return maxSum